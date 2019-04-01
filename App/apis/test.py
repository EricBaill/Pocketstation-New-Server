# -*- coding: utf-8 -*-
from flask_restful import Resource

from App.models import Point, Order, db


class Test(Resource):
    def get(self,staff_id):
        list_ = []
        point = Point.query.filter(Point.staff_id == staff_id).first()
        orders = Order.query.filter(Order.user_id == staff_id).all()
        if orders:
            for order in orders:
                list_.append(order.price)
            prices = sum(list_)
            point.sumprice = prices
            db.session.commit()
            print(point.sumprice)
