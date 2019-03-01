from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import User, db, Position, BusinessUnit


class StaffRespource(Resource):
    def get(self):
        users = User.query.all()
        list_ = []
        for user in users:
            poss = Position.query.filter(Position.id.__eq__(user.pos_id)).all()
            for pos in poss:
                bus = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos.bu_id)).all()
                for bu in bus:
                    data = {
                        'id':user.id,
                        'openid':user.openid,
                        'name':user.name,
                        'email':user.email,
                        'avatar':user.img_src,
                        'tel':user.tel,
                        'passwd':user.passwd,
                        'create_at':user.create_at,
                        'pos':{
                            'id':pos.id,
                            'name':pos.name,
                            'is_manager':pos.is_manager,
                            'bu':{
                                'id':bu.id,
                                'name':bu.name
                            }
                        }
                    }
                    list_.append(data)
        return jsonify(list_)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='pos_id', type=int)
        parser.add_argument(name='name', type=str)
        parser.add_argument(name='email', type=str)
        parser.add_argument(name='tel', type=str)
        parser.add_argument(name='passwd', type=str)
        parse = parser.parse_args()
        pos_id = parse.get('pos_id')
        name = parse.get('name')
        email = parse.get('email')
        tel = parse.get('tel')
        passwd = parse.get('passwd')
        user = User()
        user.pos_id = pos_id
        user.name = name
        user.email = email
        user.tel = tel
        user.passwd = passwd
        user.img_src = '/default/avatar_64px.png'
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print(str(e))
        user = User.query.filter(User.email.__eq__(email)).first()
        pos = Position.query.filter(Position.id.__eq__(user.pos_id)).first()
        bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos.bu_id)).first()
        data = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'avatar': user.img_src,
            'tel': user.tel,
            'passwd': user.passwd,
            'create_at': user.create_at,
            'pos': {
                'id': pos.id,
                'name': pos.name,
                'bu': {
                    'id': bu.id,
                    'name': bu.name
                }
            }
        }
        return jsonify(data)

class StaffRespource1(Resource):
    def get(self,user_id):
        user = User.query.filter(User.id.__eq__(user_id)).first()
        if user:
            num = user.dayno
            return jsonify(num)
        else:
            return jsonify({'err':'用户不存在！'})

    def patch(self,user_id):
        parser = reqparse.RequestParser()
        parser.add_argument(name='pos_id', type=int)
        parser.add_argument(name='name', type=str)
        parser.add_argument(name='email', type=str)
        parser.add_argument(name='tel', type=str)
        parser.add_argument(name='avatar', type=str)
        parse = parser.parse_args()
        pos_id = parse.get('pos_id')
        name = parse.get('name')
        email = parse.get('email')
        tel = parse.get('tel')
        avatar = parse.get('avatar')
        user = User.query.filter(User.id.__eq__(user_id)).first()
        if user:
            user.pos_id = pos_id
            user.name = name
            user.email = email
            user.tel = tel
            user.img_src = avatar
            db.session.commit()
            user = User.query.filter(User.email.__eq__(email)).first()
            pos = Position.query.filter(Position.id.__eq__(user.pos_id)).first()
            bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos.bu_id)).first()
            data = {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'avatar': user.img_src,
                'tel': user.tel,
                'passwd': user.passwd,
                'create_at': user.create_at,
                'pos': {
                    'id': pos.id,
                    'name': pos.name,
                    'bu': {
                        'id': bu.id,
                        'name': bu.name
                    }
                }
            }
            return jsonify(data)
        else:
            return jsonify({'err':404})

    def delete(self,user_id):
        user = User.query.filter(User.id.__eq__(user_id)).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'msg':'删除成功！'})
        else:
            return jsonify({'err':404})

class StaffRespource2(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='name', type=str)
        parse = parser.parse_args()
        name = parse.get('name')
        users = User.query.filter(User.name.__eq__(name)).all()
        list_ = []
        for user in users:
            pos = Position.query.filter(Position.id.__eq__(user.pos_id)).first()
            bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos.bu_id)).first()
            if user:
                data = {
                    'id': user.id,
                    'name': user.name,
                    'email': user.email,
                    'avatar': user.img_src,
                    'tel': user.tel,
                    'passwd': user.passwd,
                    'create_at': user.create_at,
                    'pos': {
                        'id': pos.id,
                        'name': pos.name,
                        'bu': {
                            'id': bu.id,
                            'name': bu.name
                        }
                    }
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])

