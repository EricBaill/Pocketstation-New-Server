from flask import jsonify, make_response
from flask_restful import Resource, reqparse

from App.models import Admin, db, BusinessUnit

parser = reqparse.RequestParser()
parser.add_argument(name='name', type=str, required=True, help='用户名不能为空')
parser.add_argument(name='email', type=str, required=True, help='邮箱不能为空')
parser.add_argument(name='bu_id', type=int)

class AdminApiResource(Resource):
    def get(self):
        # headers = {
        #     'Content-Type': 'application/json',
        #     'Access-Control-Allow-Origin': '*',
        #     'Access-Control-Allow-Methods': 'GET'
        # }
        admins = Admin.query.all()
        list_ = []
        for admin in admins:
            bu = BusinessUnit.query.filter(BusinessUnit.id == admin.bu_id).first()
            data = {
                'id': admin.id,
                'openid': admin.openid,
                'name': admin.name,
                'email': admin.email,
                'avatar': admin.avatar,
                'create_at': admin.create_at,
                'bu': {
                    'name': bu.name,
                    'id': bu.id
                }
            }
            list_.append(data)
        return jsonify(list_)
        # return make_response((jsonify(list_), 200, headers))

    def post(self):
        # headers = {
        #     'Content-Type': 'application/json',
        #     'Access-Control-Allow-Origin': '*',
        #     'Access-Control-Allow-Methods': 'POST'
        # }
        parse = parser.parse_args()
        name = parse.get('name')
        email = parse.get('email')
        bu_id = parse.get('bu_id')
        avatar = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1544011472569&di=0c979013036cc5d17214a99ea8db9d9f&imgtype=0&src=http%3A%2F%2Fpic.90sjimg.com%2Fdesign%2F00%2F67%2F59%2F63%2F58e89bee922a2.png'
        admin = Admin()
        admin.name = name
        admin.email = email
        admin.bu_id = bu_id
        admin.avatar = avatar
        try:
            db.session.add(admin)
            db.session.commit()
        except Exception as e:
            print(str(e))
        admins = Admin.query.filter(Admin.name == name).first()
        bu = BusinessUnit.query.filter(BusinessUnit.id==admins.bu_id).first()
        data = {
            'id':admins.id,
            'name':name,
            'email':email,
            'avatar':avatar,
            'create_at':admins.create_at,
            'bu':{
                'name':bu.name,
                'id':bu.id
            }
        }
        return jsonify(data)
        # return make_response((jsonify(data), 200, headers))

class AdminApiResource1(Resource):
    def put(self,admin_id):
        # headers = {
        #     'Content-Type': 'application/json',
        #     'Access-Control-Allow-Origin': '*',
        #     'Access-Control-Allow-Methods': 'PUT'
        # }
        parse = parser.parse_args()
        name = parse.get('name')
        email = parse.get('email')
        bu_id = parse.get('bu_id')
        avatar = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1544011472569&di=0c979013036cc5d17214a99ea8db9d9f&imgtype=0&src=http%3A%2F%2Fpic.90sjimg.com%2Fdesign%2F00%2F67%2F59%2F63%2F58e89bee922a2.png'

        admin = Admin.query.filter(Admin.id.__eq__(admin_id)).first()
        if admin:
            admin.name = name
            admin.email = email
            admin.avatar = avatar
            admin.bu_id = bu_id
            db.session.commit()
            bu = BusinessUnit.query.filter(BusinessUnit.id == bu_id).first()
            data = {
                'id': admin_id,
                'name': name,
                'email': email,
                'avatar': avatar,
                'create_at': admin.create_at,
                'bu': {
                    'name': bu.name,
                    'id': bu.id
                }
            }
            return jsonify(data)
            # return make_response((jsonify(data), 200, headers))
        else:
            return jsonify({'err':404})
            # return make_response((jsonify({'err':404}), 404, headers))

    def delete(self,admin_id):
        admins = Admin.query.filter(Admin.id.__eq__(admin_id)).first()
        if admins:
            db.session.delete(admins)
            db.session.commit()
            return jsonify({'msg': '删除成功！'})
        else:
            return jsonify({'msg': '暂无信息！'})

