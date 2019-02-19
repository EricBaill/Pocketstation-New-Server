from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import Position, BusinessUnit, db



class PositionResource(Resource):
    def get(self):
        poss = Position.query.all()
        list_ = []
        for pos in poss:
            bu_id = pos.bu_id
            bus = BusinessUnit.query.filter(BusinessUnit.id.__eq__(bu_id)).all()
            for bu in bus:
                data = {
                    'id':pos.id,
                    'name':pos.name,
                    'is_manager':pos.is_manager,
                    'bu':{
                        'id':bu.id,
                        'name':bu.name,
                    }
                }
                list_.append(data)
        return jsonify(list_)

class PositionResource1(Resource):
    def put(self,id):
        parser = reqparse.RequestParser()
        parser.add_argument(name='name', type=str, required=True, help='名称不能为空')
        parser.add_argument(name='bu_id', type=int)
        parse = parser.parse_args()
        name = parse.get('name')
        bu_id = parse.get('bu_id')
        poss = Position.query.filter(Position.id.__eq__(id)).first()
        if poss:
            poss.name = name
            poss.bu_id = bu_id
            db.session.commit()
            bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(bu_id)).first()
            pos = Position.query.filter(Position.name == name).first()
            data = {
                'id': pos.id,
                'name': pos.name,
                'bu': {
                    'id': bu.id,
                    'name': bu.name,
                }
            }
            return jsonify(data)
        else:
            return jsonify({})

    def delete(self,id):
        poss = Position.query.filter(Position.id.__eq__(id)).first()
        if poss:
            db.session.delete(poss)
            db.session.commit()
            return jsonify({'msg':'删除成功！'})
        else:
            return jsonify({})

class PositionResource2(Resource):
    def post(self,bu_id):
        parser = reqparse.RequestParser()
        parser.add_argument(name='name', type=str, required=True, help='名称不能为空')
        parser.add_argument(name='is_manager', type=int)
        parse = parser.parse_args()
        name = parse.get('name')
        is_manager = parse.get('is_manager')
        poss = Position()
        poss.name = name
        poss.is_manager = is_manager
        poss.bu_id = bu_id
        try:
            db.session.add(poss)
            db.session.commit()
        except Exception as e:
            print(str(e))
        bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(bu_id)).first()
        pos = Position.query.filter(Position.name == name).order_by(Position.id.desc()).first()
        data = {
            'id': pos.id,
            'name': pos.name,
            'is_manager': pos.is_manager,
            'bu': {
                'id': bu.id,
                'name': bu.name,
            }
        }
        return jsonify(data)