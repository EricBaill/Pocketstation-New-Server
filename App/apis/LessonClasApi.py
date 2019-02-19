from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import LessonClas, db

parser = reqparse.RequestParser()
parser.add_argument(name='name', type=str, required=True, help='类名不能为空')
parser.add_argument(name='img_src', type=str)

class LessonClasResource(Resource):
    def get(self):
        les_clss = LessonClas.query.all()
        list_ = []
        for les_cls in les_clss:
            data = {
                'id':les_cls.id,
                'name':les_cls.name,
                'img_src':les_cls.img_src
            }
            list_.append(data)
        return jsonify(list_)

    def post(self):
        parse = parser.parse_args()
        name = parse.get('name')
        img_src = parse.get('img_src')
        les_cls = LessonClas()
        les_cls.name = name
        les_cls.img_src = img_src
        try:
            db.session.add(les_cls)
            db.session.commit()
        except Exception as e:
            print(str(e))
        les_clss = LessonClas.query.filter(LessonClas.name.__eq__(name)).first()
        data = {
            'id':les_clss.id,
            'name':name,
            'img_src':img_src
        }
        return jsonify(data)

class LessonClasResource1(Resource):
    def put(self,id):
        parse = parser.parse_args()
        name = parse.get('name')
        img_src = parse.get('img_src')
        les_clss = LessonClas.query.filter(LessonClas.id.__eq__(id)).first()
        if les_clss:
            les_clss.name = name
            les_clss.img_src = img_src
            db.session.commit()
            data = {
                'id':id,
                'name':name,
                'img_src':img_src
            }
            return jsonify(data)
        else:
            return jsonify({})

    def delete(self,id):
        les_clss = LessonClas.query.filter(LessonClas.id.__eq__(id)).first()
        if les_clss:
            db.session.delete(les_clss)
            db.session.commit()
            return jsonify({'msg':'删除成功！'})
        else:
            return jsonify({})
