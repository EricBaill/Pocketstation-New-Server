# -*- coding: utf-8 -*-
from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import Production, User, Shopcart, db

parser = reqparse.RequestParser()
parser.add_argument(name='number', type=str)
parser.add_argument(name='pro_id', type=int)
parser.add_argument(name='staff_id', type=int)

class ShopCart_(Resource):
    def post(self):
        pass
        # parse = parser.parse_args()
        # number = parse.get('number')
        # pro_id = parse.get('pro_id')
        # staff_id = parse.get('staff_id')
        # pro = Production.query.filter(Production.id==pro_id).first()
        # if pro:
        #     cart = Shopcart()
        #     cart.product_id = pro_id
        #     cart.user_id = staff_id
        #     cart.number = number
        #     db.session.add(cart)
        #     db.session.commit()
        #     return jsonify({'msg':'添加成功'})
        # else:
        #     return jsonify({})


class GetShopcart(Resource):
    def get(self,staff_id):
        pass
        # list_ = []
        # user = User.query.filter(User.id==staff_id).first()
        # carts = Shopcart.query.filter(Shopcart.user_id==staff_id).all()
        # if carts:
        #     for cart in carts:
        #         pro = Production.query.filter(Production.id==cart.product_id).first()
        #         if pro:
        #             data = {
        #                 'id': pro.id,
        #                 'name': pro.name,
        #                 'price': pro.price,
        #                 'product_no': pro.product_no,
        #                 'img': pro.img,
        #                 'date': pro.product_date,
        #                 'content': pro.content,
        #                 'instruction': pro.instruction
        #             }
        #             list_.append(data)
        #         else:
        #             return jsonify([])
        #     return jsonify(list_)
        # else:
        #     return jsonify([])
