from flask import jsonify
from flask_restful import Resource, reqparse
from App.models import GratitudeStar, User, Position, BusinessUnit, Gratitude, db


class GratStarResource(Resource):
    def get(self):
        list_1 = []
        gratstars = GratitudeStar.query.all()
        for gratstar in gratstars:
            list_1.append(gratstar)
        user0 = User.query.filter(User.id.__eq__(list_1[-1].staff_id)).first()
        pos0 = Position.query.filter(Position.id.__eq__(user0.pos_id)).first()
        bu0 = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos0.bu_id)).first()
        if user0:
            data0 = {
                'staff':{
                    'id':user0.id,
                    'name':user0.name,
                    'email':user0.email,
                    'avatar':user0.img_src,
                },
                'pos':{
                    'name':pos0.name,
                },
                'bu':{
                    'name':bu0.name,
                    'id':bu0.id
                },
                'id':list_1[-1].id,
                'create_at':list_1[-1].create_at,
                'year_month':list_1[-1].year_month
            }
            return jsonify(data0)
        else:
            return jsonify({})

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='staff_id', type=int)
        parser.add_argument(name='year_month', type=str)
        parse = parser.parse_args()
        staff_id = parse.get('staff_id')
        year_month = parse.get('year_month')
        gratstars = GratitudeStar()
        gratstars.staff_id = staff_id
        gratstars.year_month = year_month
        db.session.add(gratstars)
        db.session.commit()
        gratstar = GratitudeStar.query.filter(GratitudeStar.staff_id.__eq__(staff_id)).first()
        user = User.query.filter(User.id.__eq__(staff_id)).first()
        pos = Position.query.filter(Position.id.__eq__(user.pos_id)).first()
        bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos.bu_id)).first()
        data = {
            'staff': {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'avatar': user.img_src,
            },
            'pos': {
                'name': pos.name,
            },
            'bu': {
                'name': bu.name,
                'id': bu.id
            },
            'id': gratstar.id,
            'create_at': gratstar.create_at,
            'year_month': year_month
        }
        return jsonify(data)

