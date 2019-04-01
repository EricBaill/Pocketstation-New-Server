# -*- coding: utf-8 -*-
from flask import jsonify
from flask_restful import Resource, reqparse
import datetime
import time
from App.models import Point, Order, db, Production

parser = reqparse.RequestParser()
parser.add_argument(name='staff_id', type=int)
parser.add_argument(name='number', type=str)
parser.add_argument(name='price', type=float)
parser.add_argument(name='address', type=str)
parser.add_argument(name='phone', type=str)
parser.add_argument(name='consignee', type=str)


class Order_(Resource):
    def post(self):
        list_ = []
        parse = parser.parse_args()
        staff_id = parse.get('staff_id')
        number = parse.get('number')
        price = parse.get('price')
        address = parse.get('address')
        phone = parse.get('phone')
        consignee = parse.get('consignee')

        datetime_now = datetime.datetime.now()
        date_stamp = str(int(time.mktime(datetime_now.timetuple())))
        data_microsecond = str("%06d" % datetime_now.microsecond)
        date_stamp = date_stamp + data_microsecond

        order = Order()
        order.order_no = date_stamp
        order.price = price
        order.user_id = staff_id
        order.number = number
        order.address = address
        order.phone = phone
        order.consignee = consignee
        db.session.add(order)
        db.session.commit()

        point = Point.query.filter(Point.staff_id==staff_id).first()
        orders = Order.query.filter(Order.user_id == staff_id).all()
        if orders:
            for order in orders:
                list_.append(order.price)
            prices = sum(list_)
            print(prices)
            point.sumprice = prices
            print(point.sumprice)
            db.session.commit()
        else:
            pass

        return jsonify({'msg':'添加成功'})

class GetOrder(Resource):
    def get(self,staff_id):
        orders = Order.query.filter(Order.user_id==staff_id).all()
        list_ = []
        if orders:
            for order in orders:
                list_s = eval(order.number)
                for i in range(len(list_s)):
                    pro_id = list_s[i]['id']
                    counts = list_s[i]['counts']
                    pro = Production.query.filter(Production.id==pro_id).first()
                    data = {
                        'order_id':order.id,
                        'order_no':order.order_no,
                        'price':order.price,
                        'create_at':order.create_at,
                        'status':order.status,
                        'productions':{
                            'id':pro_id,
                            'name': pro.name,
                            'img':pro.img,
                            'number':counts,
                            'price':pro.price
                        }
                    }
                    list_.append(data)
            list2 = []
            for i in range(len(list_)):
                if list_[i] != {}:
                    re_list = []
                    re_list.append(list_[i].get('productions'))
                    for j in range(i + 1, len(list_)):
                        if list_[i].get('order_id') == list_[j].get('order_id'):
                            re_list.append(list_[j].get('productions'))
                            list_[i]['productions'] = re_list
                            list_[j] = {}
                    if type(list_[i]['productions']) == list:
                        pass
                    else:
                        list_[i]['productions'] = [list_[i]['productions']]
                    list2.append(list_[i])
            return jsonify(list2)
        else:
            return jsonify([])


class GetOrder01(Resource):
    def get(self,id):
        list_ = []
        order = Order.query.filter(Order.id==id).first()
        if order:
            list_s = eval(order.number)
            for i in range(len(list_s)):
                pro_id = list_s[i]['id']
                counts = list_s[i]['counts']
                pro = Production.query.filter(Production.id == pro_id).first()
                data = {
                    'order_id': order.id,
                    'order_no': order.order_no,
                    'address':order.address,
                    'phone':order.phone,
                    'consignee':order.consignee,
                    'price': order.price,
                    'create_at': order.create_at,
                    'status': order.status,
                    'productions': {
                        'id': pro_id,
                        'name': pro.name,
                        'img': pro.img,
                        'number': counts,
                        'price': pro.price
                    }
                }
                list_.append(data)
            list2 = []
            for i in range(len(list_)):
                if list_[i] != {}:
                    re_list = []
                    re_list.append(list_[i].get('productions'))
                    for j in range(i + 1, len(list_)):
                        if list_[i].get('order_id') == list_[j].get('order_id'):
                            re_list.append(list_[j].get('productions'))
                            list_[i]['productions'] = re_list
                            list_[j] = {}
                    if type(list_[i]['productions']) == list:
                        pass
                    else:
                        list_[i]['productions'] = [list_[i]['productions']]
                    list2.append(list_[i])
            return jsonify(list2)
        else:
            return jsonify([])

class DelOrder(Resource):
    def delete(self,id):
        order = Order.query.filter(Order.id==id).first()
        if order:
            db.session.delete(order)
            db.session.commit()
            return jsonify({'msg':'删除成功'})
        else:
            return jsonify({})


class GetallOrders(Resource):
    def get(self):
        list_ = []
        orders = Order.query.all()
        if orders:
            for order in orders:
                list_s = eval(order.number)
                for i in range(len(list_s)):
                    pro_id = list_s[i]['id']
                    counts = list_s[i]['counts']
                    pro = Production.query.filter(Production.id == pro_id).first()
                    data = {
                        'order_id': order.id,
                        'order_no': order.order_no,
                        'address': order.address,
                        'phone': order.phone,
                        'consignee': order.consignee,
                        'price': order.price,
                        'create_at': order.create_at,
                        'status': order.status,
                        'productions': {
                            'id': pro_id,
                            'name': pro.name,
                            'img': pro.img,
                            'number': counts,
                            'price': pro.price
                        }
                    }
                    list_.append(data)
            list2 = []
            for i in range(len(list_)):
                if list_[i] != {}:
                    re_list = []
                    re_list.append(list_[i].get('productions'))
                    for j in range(i + 1, len(list_)):
                        if list_[i].get('order_id') == list_[j].get('order_id'):
                            re_list.append(list_[j].get('productions'))
                            list_[i]['productions'] = re_list
                            list_[j] = {}
                    if type(list_[i]['productions']) == list:
                        pass
                    else:
                        list_[i]['productions'] = [list_[i]['productions']]
                    list2.append(list_[i])
            return jsonify(list2)
        else:
            return jsonify([])

class OrderStatus(Resource):
    def get(self,id):
        order = Order.query.filter(Order.id==id).first()
        if order:
            order.status = 1
            db.session.commit()
            return jsonify({'msg':'以发货！'})
        else:
            return jsonify({})
