from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import Experience, Admin, DealerTraining, db

parser = reqparse.RequestParser()
parser.add_argument(name='title',type=str,required=True,help='标题不能为空')
parser.add_argument(name='content',type=str,required=True,help='内容不能为空')

class ExperienceResource(Resource):
    def get(self,course_id):
        experiences = Experience.query.filter(Experience.dealer_training_id.__eq__(course_id)).all()
        list_ = []
        for experience in experiences:
            admin = Admin.query.filter(Admin.id.__eq__(experience.admin_id)).first()
            data = {
                'dealer':{
                    'name': admin.name,
                    'avatar': admin.avatar,
                },
                    'id': experience.id,
                    'title': experience.title,
                    'content': experience.content,
                    'type':experience.type,
                    'create_at':experience.create_at,
            }
            list_.append(data)
        print(list_)
        return jsonify(list_)

class ExperienceResource1(Resource):
    def put(self,course_id,gains_id):
        experiences = Experience.query.filter(Experience.dealer_training_id == course_id).first()
        if experiences:
            experience = Experience.query.filter(Experience.id == gains_id).first()
            if experience.type == 1:
                experience.type = 0
            else:
                experience.type = 1
            db.session.add(experience)
            db.session.commit()
        return {'msg':'状态修改成功'}

class ExperienceResource2(Resource):
    def post(self,course_id,user_id):
        parse = parser.parse_args()
        title = parse.get('title')
        content = parse.get('content')
        exper= Experience()
        exper.dealer_training_id = course_id
        exper.admin_id = user_id
        exper.title = title
        exper.content = content
        db.session.add(exper)
        db.session.commit()

        experience = Experience.query.filter(Experience.dealer_training_id == course_id).order_by(Experience.id.desc()).first()
        admins = Admin.query.filter(Admin.id == user_id).all()
        list_ = []
        for admin in admins:
            data = {
                'dealer': {
                    'name': admin.name,
                    'avatar': admin.avatar,
                },
                'id': experience.id,
                'title': title,
                'content': content,
                'type': experience.type,
                'create_at': experience.create_at,
            }
            list_.append(data)
            return jsonify(data)

class ExperienceResource3(Resource):
    def get(self,course_id):
        experiences = Experience.query.filter(Experience.dealer_training_id == course_id).all()
        list_ = []
        if experiences:
            for experience in experiences:
                if experience.type == 1:
                    admins = Admin.query.filter(Admin.id==experience.admin_id).all()
                    for admin in admins:
                        data = {
                            'id':experience.id,
                            'dealer':{
                                'name': admin.name,
                                'avatar': admin.avatar
                            },
                            'title': experience.title,
                            'content': experience.content,
                            'type': experience.type,
                            'create_at': experience.create_at,
                        }
                    list_.append(data)
            return jsonify(list_)