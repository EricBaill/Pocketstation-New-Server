from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import Operation, LessonClas, db

parser = reqparse.RequestParser()
parser.add_argument(name='name', type=str, required=True, help='类名不能为空')
parser.add_argument(name='cls_id', type=int)
parser.add_argument(name='img_src', type=str)

class OperationResource(Resource):
    def get(self):
        opers = Operation.query.all()
        list_ = []
        for oper in opers:
            les_cls = LessonClas.query.filter(LessonClas.id==oper.cls_id).first()
            data = {
                'id':oper.id,
                'name':oper.name,
                'img_src':oper.img_src,
                'cls':{
                    'id':les_cls.id,
                    'name':les_cls.name
                }
            }
            list_.append(data)
        return jsonify(list_)

    def post(self):
        parse = parser.parse_args()
        name = parse.get('name')
        cls_id = parse.get('cls_id')
        img_src = parse.get('img_src')
        opers = Operation()
        opers.name = name
        opers.cls_id = cls_id
        opers.img_src = img_src
        try:
            db.session.add(opers)
            db.session.commit()
        except Exception as e:
            print(str(e))
        les_cls = LessonClas.query.filter(LessonClas.id == cls_id).first()
        operss = Operation.query.filter(Operation.name.__eq__(name)).first()
        data = {
            'id': operss.id,
            'name': name,
            'img_src': img_src,
            'cls': {
                'id': les_cls.id,
                'name': les_cls.name
            }
        }
        return jsonify(data)

class OperationResource1(Resource):
    def put(self,id):
        parse = parser.parse_args()
        name = parse.get('name')
        img_src = parse.get('img_src')
        opers = Operation.query.filter(Operation.id.__eq__(id)).first()
        if opers:
            opers.name = name
            opers.img_src = img_src
            db.session.commit()
            operss = Operation.query.filter(Operation.name.__eq__(name)).first()
            les_cls = LessonClas.query.filter(LessonClas.id == operss.cls_id).first()
            data = {
                'id': operss.id,
                'name': name,
                'img_src': img_src,
                'cls': {
                    'id': les_cls.id,
                    'name': les_cls.name
                }
            }
            return jsonify(data)
        else:
            return jsonify({'err': '暂无信息！'})

    def delete(self,id):
        opers = Operation.query.filter(Operation.id.__eq__(id)).first()
        if opers:
            db.session.delete(opers)
            db.session.commit()
            return jsonify({'msg':'删除成功！'})
        else:
            return jsonify({'err': '暂无信息！'})

#前端页面
class OperationResource2(Resource):
    def get(self,cls_id):
        opers = Operation.query.filter(Operation.cls_id.__eq__(cls_id)).all()
        list_ = []
        if opers:
            for oper in opers:
                les_cls = LessonClas.query.filter(LessonClas.id.__eq__(oper.cls_id)).first()
                data = {
                    'cls':{
                        'id':les_cls.id,
                        'name':les_cls.name
                    },
                    'id':oper.id,
                    'name':oper.name,
                    'img_src':oper.img_src
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify({'err': '暂无信息！'})
