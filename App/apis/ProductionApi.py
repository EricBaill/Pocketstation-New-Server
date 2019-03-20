# -*- coding: utf-8 -*-
from flask import jsonify
from flask_restful import Resource

from App.models import Production


class Production_(Resource):
    def get(self):
        list_ = []
        pros = Production.query.all()
        if pros:
            for pro in pros:
                data = {
                    'id':pro.id,
                    'name':pro.name,
                    'price':pro.price,
                    'product_no':pro.product_no,
                    'img':pro.img,
                    'date':pro.product_date,
                    'content':pro.content,
                    'instruction':pro.instruction
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])


class Production_01(Resource):
    def get(self,id):
        pro = Production.query.filter(Production.id==id).first()
        if pro:
            data = {
                'id': pro.id,
                'name': pro.name,
                'price': pro.price,
                'product_no': pro.product_no,
                'img': pro.img,
                'date': pro.product_date,
                'content': pro.content,
                'instruction': pro.instruction
            }
            return jsonify(data)
        else:
            return jsonify({})
