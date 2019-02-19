from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import BusinessUnit, db

parser = reqparse.RequestParser()
parser.add_argument(name='name', type=str, required=True, help='名称不能为空')

class BuResource(Resource):
    def get(self):
        bus = BusinessUnit.query.all()
        list_ = []
        for bu in bus:
            data = {
                'id':bu.id,
                'name':bu.name
            }
            list_.append(data)
        return jsonify(list_)

    def post(self):
        parse = parser.parse_args()
        name = parse.get('name')
        bu = BusinessUnit()
        bu.name = name
        db.session.add(bu)
        db.session.commit()
        bus = BusinessUnit.query.filter(BusinessUnit.name == name).order_by(BusinessUnit.id.desc()).first()
        data = {
            'id': bus.id,
            'name': name
        }
        return jsonify(data)

class BuResource1(Resource):
    def put(self,id):
        parse = parser.parse_args()
        name = parse.get('name')
        bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(id)).first()
        if bu:
            bu.name = name
            db.session.commit()
            data = {
                'id': id,
                'name': name
            }
            return jsonify(data)
        else:
            return jsonify({"err":404})

    def delete(self,id):
        bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(id)).first()
        if bu:
            db.session.delete(bu)
            db.session.commit()
            return jsonify({'msg':'删除成功！'})
        else:
            return jsonify({'err':'404'})