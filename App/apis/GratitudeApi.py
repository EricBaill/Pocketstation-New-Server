import json

import requests
from flask import jsonify
from flask_restful import Resource, reqparse

from App.apis.TokenApi import logger
from App.models import Gratitude, User, Position, BusinessUnit, db


class GratitudeResource(Resource):
    def get(self):
        grats = Gratitude.query.all()
        list_ = []
        for grat in grats:
            from_users = User.query.filter(User.id.__eq__(grat.from_id)).all()
            to_users = User.query.filter(User.id.__eq__(grat.to_id)).all()
            for from_user in from_users:
                for to_user in to_users:
                    data = {
                        "content": grat.content,
                        "staff_from": {
                            "name": from_user.name,
                            "avatar": from_user.img_src
                        },
                        "staff_to": {
                            "name": to_user.name,
                            "avatar": to_user.img_src
                        },
                        "create_at": grat.create_at,
                        "id": grat.id
                    }
                    list_.append(data)
        return jsonify(list_)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='_from', type=str, required=True, help='感恩者不能为空')
        parser.add_argument(name='to', type=str, required=True, help='被感恩者不能为空')
        parser.add_argument(name='content', type=str, required=True, help='内容不能为空')
        parse = parser.parse_args()
        _from = parse.get('_from')
        to = parse.get('to')
        content = parse.get('content')
        grat = Gratitude()
        grat.from_id = _from
        grat.to_id = to
        grat.content = content
        db.session.add(grat)
        db.session.commit()

        appid = 'wxc7cf4e85ecbf8282'
        secret = 'bafb0339afa3db639000a92ae15ff072'
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(appid,
                                                                                                               secret)
        response = requests.get(url)
        logger.info('post[%s]=>[%s][%s][%s]' % (
            appid, secret, response.status_code, response.text
        ))
        resData = response.json()
        access_token = resData['access_token']

        u = User.query.filter(User.id.__eq__(to)).first()
        u1 = User.query.filter(User.id.__eq__(_from)).first()
        u_openid = u.openid

        url1 = 'https://api.weixin.qq.com/cgi-bin/template/get_all_private_template?access_token={}'.format(access_token)
        response = requests.get(url1)
        logger.info('post[%s]=>[%s][%s]' % (
            access_token, response.status_code, response.text
        ))
        resData = response.json()

        openid = u_openid
        template_id = resData['template_list'][-1]['template_id']
        url = 'https://pocketstation.cn/'
        msg = {
            "touser": openid,
            "template_id": template_id,
            "url": url,
            "data": {
                "first": {
                    "value": "刚刚有人偷偷感恩您啦！",
                    "color": "#000"
                },
                "keyword1": {
                    "value": u1.name,
                    "color": "#000"
                },
                "keyword2": {
                    "value": content,
                    "color": "#000"
                },
                # "remark": {
                #     "value": "点击查看详情",
                #     "color": "#000"
                # }
            }
        }
        json_data = json.dumps(msg)
        url4 = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s' % access_token
        r = requests.post(url4, json_data)
        print(json.loads(r.text))

        from_users = User.query.filter(User.id.__eq__(_from)).first()
        to_users = User.query.filter(User.id.__eq__(to)).first()
        grats = Gratitude.query.all()
        data = {
            "content": grat.content,
            "staff_from": {
                "name": from_users.name,
                "avatar": from_users.img_src
            },
            "staff_to": {
                "name": to_users.name,
                "avatar": to_users.img_src
            },
            "create_at": grats[-1].create_at,
            "id": grats[-1].id
        }
        return jsonify(data)

class GratitudeResource1(Resource):
    def get(self):
        list_ = []
        grats = Gratitude.query.all()
        if len(grats)>=5:
            for i in [-1,-2,-3,-4,-5]:
                _to = grats[i].to_id
                to_user = User.query.filter(User.id.__eq__(_to)).first()
                if to_user:
                    pos = Position.query.filter(Position.id.__eq__(to_user.pos_id)).first()
                    if pos:
                        bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos.bu_id)).first()
                        if to_user:
                            data0 = {
                                'staff': {
                                    'id': to_user.id,
                                    'name': to_user.name,
                                    'email': to_user.email,
                                    'avatar': to_user.img_src,
                                },
                                'pos': {
                                    'name': pos.name,
                                },
                                'bu': {
                                    'name': bu.name,
                                    'id': bu.id
                                },
                            }
                            list_.append(data0)
            return jsonify(list_)
        elif len(grats)==4:
            for i in [-1,-2,-3,-4]:
                _to = grats[i].to_id
                to_user = User.query.filter(User.id.__eq__(_to)).first()
                if to_user:
                    pos = Position.query.filter(Position.id.__eq__(to_user.pos_id)).first()
                    if pos:
                        bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos.bu_id)).first()
                        if to_user:
                            data0 = {
                                'staff': {
                                    'id': to_user.id,
                                    'name': to_user.name,
                                    'email': to_user.email,
                                    'avatar': to_user.img_src,
                                },
                                'pos': {
                                    'name': pos.name,
                                },
                                'bu': {
                                    'name': bu.name,
                                    'id': bu.id
                                },
                            }
                            list_.append(data0)
            return jsonify(list_)
        elif len(grats) == 3:
            for i in [-1,-2,-3]:
                _to = grats[i].to_id
                to_user = User.query.filter(User.id.__eq__(_to)).first()
                if to_user:
                    pos = Position.query.filter(Position.id.__eq__(to_user.pos_id)).first()
                    if pos:
                        bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos.bu_id)).first()
                        if to_user:
                            data0 = {
                                'staff': {
                                    'id': to_user.id,
                                    'name': to_user.name,
                                    'email': to_user.email,
                                    'avatar': to_user.img_src,
                                },
                                'pos': {
                                    'name': pos.name,
                                },
                                'bu': {
                                    'name': bu.name,
                                    'id': bu.id
                                },
                            }
                            list_.append(data0)
            return jsonify(list_)
        elif len(grats) == 2:
            for i in [-1,-2]:
                _to = grats[i].to_id
                to_user = User.query.filter(User.id.__eq__(_to)).first()
                if to_user:
                    pos = Position.query.filter(Position.id.__eq__(to_user.pos_id)).first()
                    if pos:
                        bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos.bu_id)).first()
                        if to_user:
                            data0 = {
                                'staff': {
                                    'id': to_user.id,
                                    'name': to_user.name,
                                    'email': to_user.email,
                                    'avatar': to_user.img_src,
                                },
                                'pos': {
                                    'name': pos.name,
                                },
                                'bu': {
                                    'name': bu.name,
                                    'id': bu.id
                                },
                            }
                            list_.append(data0)
            return jsonify(list_)
        elif len(grats) == 1:
            _to = grats[-1].to_id
            to_user = User.query.filter(User.id.__eq__(_to)).first()
            if to_user:
                pos = Position.query.filter(Position.id.__eq__(to_user.pos_id)).first()
                if pos:
                    bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos.bu_id)).first()
                    if to_user:
                        data0 = {
                            'staff': {
                                'id': to_user.id,
                                'name': to_user.name,
                                'email': to_user.email,
                                'avatar': to_user.img_src,
                            },
                            'pos': {
                                'name': pos.name,
                            },
                            'bu': {
                                'name': bu.name,
                                'id': bu.id
                            },
                        }
                        list_.append(data0)
            return jsonify(list_)
        else:
            return jsonify([])

    #搜索感恩记录
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='_from', type=str, required=True, help='感恩者不能为空')
        parser.add_argument(name='_to', type=str, required=True, help='被感恩者不能为空')
        parse = parser.parse_args()
        _from = parse.get('_from')
        _to = parse.get('_to')
        from_users = User.query.filter(User.name.__eq__(_from)).all()
        to_users = User.query.filter(User.name.__eq__(_to)).all()
        list_ = []
        for from_user in from_users:
            for to_user in to_users:
                grats = Gratitude.query.filter(Gratitude.from_id.__eq__(from_user.id), Gratitude.to_id.__eq__(to_user.id)).all()
                if grats:
                    for grat in grats:
                        data = {
                            'id': grat.id,
                            "create_at": grat.create_at,
                            "id": grat.id,
                            "staff_from": {
                                "name": from_user.name,
                                "avatar": from_user.img_src
                            },
                            "staff_to": {
                                "name": to_user.name,
                                "avatar": to_user.img_src
                            },
                        }
                        list_.append(data)
                    return jsonify(list_)
                else:
                    return jsonify([])

class GratitudeResource2(Resource):
    def delete(self,id):
        grat = Gratitude.query.filter(Gratitude.id.__eq__(id)).first()
        if grat:
            db.session.delete(grat)
            db.session.commit()
            return jsonify({'msg':'删除成功！'})
        else:
            return jsonify({'err':404})

class GratitudeResource3(Resource):
    def get(self,from_id,to_id):
        grats = Gratitude.query.filter(Gratitude.from_id.__eq__(from_id),Gratitude.to_id.__eq__(to_id)).all()
        list_ = []
        if grats:
            for grat in grats:
                from_user = User.query.filter(User.id.__eq__(grat.from_id)).first()
                to_user = User.query.filter(User.id.__eq__(grat.to_id)).first()
                data = {
                    'id':grat.id,
                    "create_at": grat.create_at,
                    "id": grat.id,
                    "staff_from": {
                        "name": from_user.name,
                        "avatar": from_user.img_src
                    },
                    "staff_to": {
                        "name": to_user.name,
                        "avatar": to_user.img_src
                    },
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])


class GratitudeResource4(Resource):
    def get(self,_to):
        grats = Gratitude.query.filter(Gratitude.to_id.__eq__(_to)).all()
        if grats:
            num = len(grats)
            return jsonify(num)
        else:
            return jsonify(0)

class GratitudeResource5(Resource):
    def get(self,_from):
        grats = Gratitude.query.filter(Gratitude.from_id.__eq__(_from)).all()
        if grats:
            num = len(grats)
            return jsonify(num)
        else:
            return jsonify(0)