from flask import Flask, g, jsonify, request
from pyasn1.debug import Debug
from werkzeug.utils import secure_filename

import logging_config
import traceback
from PIL import Image
import os
import App.ext
from App.apis import api

from uploadfile import uploadfile

logging_config.init()
import json

ALLOWED_EXTENSIONS = set(['gif', 'png', 'jpg', 'jpeg', 'bmp', 'mp4', 'ogg', 'pdf'])
IGNORED_FILES = set(['.gitignore'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def gen_file_name(filename):
    """
    If file was exist already, rename it and return a new name
    """

    i = 1
    while os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
        name, extension = os.path.splitext(filename)
        filename = '%s_%s%s' % (name, str(i), extension)
        i += 1

    return filename


def create_thumbnail(image):
    try:
        base_width = 80
        img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], image))
        w_percent = (base_width / float(img.size[0]))
        h_size = int((float(img.size[1]) * float(w_percent)))
        img = img.resize((base_width, h_size), Image.ANTIALIAS)
        img.save(os.path.join(app.config['THUMBNAIL_FOLDER'], image))

        return True

    except:
        print(traceback.format_exc())
        return False


def create_app(cfg_cls):
    # app = Flask(__name__, static_folder="s")
    # app.config.from_object(cfg_cls)
    # ext.init_app(app)
    # api.init_app(app)
    #
    # @ext.token_auth.verify_token
    # def verify_token(token):
    #
    #     status, user = verify_auth_token(token)
    #     if status:
    #         g.current_user = user
    #         return True
    #     return False
    #
    # @app.errorhandler(401)
    # def err401(e):
    #     return jsonify({"msg": "Not Authorized"}), 401

    @app.route("/upload", methods=['GET', 'POST'])
    def upload():
        if request.method == 'POST':
            files = request.files['file']

            if files:
                # filename = secure_filename(files.filename)
                filename = files.filename
                filename = gen_file_name(filename)
                mime_type = files.content_type

                if not allowed_file(files.filename):
                    result = uploadfile(name=filename, type=mime_type, size=0, not_allowed_msg="File type not allowed")

                else:
                    # save file to disk
                    uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    files.save(uploaded_file_path)

                    # create thumbnail after saving
                    if mime_type.startswith('image'):
                        create_thumbnail(filename)

                    # get file size after saving
                    size = os.path.getsize(uploaded_file_path)

                    # return json for js call back
                    result = uploadfile(name=filename, type=mime_type, size=size)

                return json.dumps({"files": [result.get_file()]})

        if request.method == 'GET':
            # get all file in ./data directory
            files = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) if
                     os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], f)) and f not in IGNORED_FILES]

            file_display = []

            for f in files:
                size = os.path.getsize(os.path.join(app.config['UPLOAD_FOLDER'], f))
                file_saved = uploadfile(name=f, size=size)
                file_display.append(file_saved.get_file())

            return json.dumps({"files": file_display})

    @app.route("/upload/<filename>", methods=["DELETE"])
    def delete_upload(filename: str):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        thumbnailpath = os.path.join(app.config['THUMBNAIL_FOLDER'], filename)
        os.path.exists(filepath) and os.remove(filepath)
        os.path.exists(thumbnailpath) and os.remove(thumbnailpath)
        return "ok"

    return app


app = create_app(Debug)

if __name__ == "__main__":
    app.run(port=5001, host="0.0.0.0")