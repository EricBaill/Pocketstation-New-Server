from flask_restful import Resource, reqparse
from sqlalchemy import extract, and_

from App.models import User, db, Admin


class LoginNumber(Resource):
    pass
    # def post(self):
    #     parser = reqparse.RequestParser()
    #     parser.add_argument(name='id', type=int)
    #     parser.add_argument(name='types', type=str)
    #     parser.add_argument(name='years', type=str)
    #     parser.add_argument(name='months', type=str)
    #     parser.add_argument(name='days', type=str)
    #     parse = parser.parse_args()
    #     id = parse.get('id')
    #     types = parse.get('types')
    #     years = parse.get('years')
    #     months = parse.get('months')
    #     days = parse.get('days')
    #     if types == 'staff':
    #         user = User.query.filter(User.id.__eq__(id),and_(
    #             extract('year', User.update_time)==years,
    #             extract('month', User.update_time)==months,
    #             extract('day', User.update_time) == days
    #         )).first()
    #         if user:
    #             user.number = user.number+1
    #             user.dayno = user.dayno+1
    #             if user.dayno >= 5:
    #                 user.dayno = 5
    #             db.session.commit()
    #         else:
    #             user = User.query.filter(User.id.__eq__(id)).first()
    #             user.dayno = 1
    #             user.number = user.number + 1
    #             if user.dayno >= 5:
    #                 user.dayno = 5
    #             db.session.commit()
    #
    #     elif types == 'dealer':
    #         admin =  Admin.query.filter(Admin.id.__eq__(id)).first()
    #         admin.number = admin.number+1
    #         db.session.commit()
    #     else:
    #         pass
    #
