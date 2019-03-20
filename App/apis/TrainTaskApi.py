import datetime
import json
from sqlalchemy import extract, and_

import requests
from flask import jsonify
from flask_restful import Resource, reqparse

from App.apis.TokenApi import logger
from App.models import TrainingTask, db, User, Lesson, Operation, LessonClas


class TrainTaskResource(Resource):
    def get(self):
        traintasks = TrainingTask.query.all()
        list_ = []
        if traintasks:
            for traintask in traintasks:
                user = User.query.filter(User.id.__eq__(traintask.staff_id)).first()
                lsn = Lesson.query.filter(Lesson.id.__eq__(traintask.lsn_id)).first()
                oper = Operation.query.filter(Operation.id.__eq__(lsn.oper_id)).first()
                lsn_cls = LessonClas.query.filter(LessonClas.id.__eq__(oper.cls_id)).first()
                if user.lesson_:
                    data = {
                        'id':traintask.id,
                        'limit':traintask.limit,
                        'percent':traintask.percent,
                        'create_at':traintask.create_at,
                        'finish_at':traintask.finish_at,
                        "days_gone": 120,
                        'staff':{
                            'id':user.id,
                            'name':user.name,
                            'email':user.email,
                            'tel':user.tel,
                            'status':user.lesson_,
                            },
                        'lsn': {
                            'id': lsn.id,
                            'name': lsn.name,
                            'oprt': {
                                'id': oper.id,
                                'name': oper.name,
                                'cls': {
                                    'id': lsn_cls.id,
                                    'name': lsn_cls.name
                                }
                            }
                        }
                    }
                    list_.append(data)
                else:
                    data = {
                        'id': traintask.id,
                        'limit': traintask.limit,
                        'percent': traintask.percent,
                        'create_at': traintask.create_at,
                        'finish_at': traintask.finish_at,
                        "days_gone": 120,
                        'staff': {
                            'id': user.id,
                            'name': user.name,
                            'email': user.email,
                            'tel': user.tel,
                            'status': int(0),
                        },
                        'lsn': {
                            'id': lsn.id,
                            'name': lsn.name,
                            'oprt': {
                                'id': oper.id,
                                'name': oper.name,
                                'cls': {
                                    'id': lsn_cls.id,
                                    'name': lsn_cls.name
                                }
                            }
                        }
                    }
                    list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='limit', type=int)
        parser.add_argument(name='lsn_id', type=int)
        parser.add_argument(name='staff_id', type=int)
        parse = parser.parse_args()
        lsn_id = parse.get('lsn_id')
        staff_id = parse.get('staff_id')
        limit = parse.get('limit')

        appid = 'wxc7cf4e85ecbf8282'
        secret = 'bafb0339afa3db639000a92ae15ff072'

        user = User.query.filter(User.id==staff_id).first()
        lesson = Lesson.query.filter(Lesson.id==lsn_id).first()
        teacher = User.query.filter(User.id==lesson.lecturer_id).first()
        task = TrainingTask.query.filter(TrainingTask.staff_id==staff_id,TrainingTask.lsn_id==lsn_id).first()
        if task:
            return jsonify({'msg':'任务已存在！'})
        else:
            if teacher:
                if user and user.openid:
                    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(
                        appid,
                        secret)
                    response = requests.get(url)
                    logger.info('post[%s]=>[%s][%s][%s]' % (
                        appid, secret, response.status_code, response.text
                    ))
                    resData = response.json()
                    access_token = resData['access_token']
                    u_openid = user.openid
                    url1 = 'https://api.weixin.qq.com/cgi-bin/template/get_all_private_template?access_token={}'.format(
                        access_token)
                    response = requests.get(url1)
                    logger.info('post[%s]=>[%s][%s]' % (
                        access_token, response.status_code, response.text
                    ))
                    resData = response.json()

                    openid = u_openid
                    template_id = resData['template_list'][-1]['template_id']
                    url = 'https://pocketstation.cn/'
                    time_ = datetime.datetime.now().strftime('%F %T')
                    msg = {
                        "touser": openid,
                        "template_id": template_id,
                        "url": url,
                        "data": {
                            "first": {
                                "value": "你有新的学习任务，请查收。",
                                "color": "#000"
                            },
                            "keyword1": {
                                "value": "口袋加油站",
                                "color": "#000"
                            },
                            "keyword2": {
                                "value": teacher.name,
                                "color": "#000"
                            },
                            "keyword3": {
                                "value": lesson.name,
                                "color": "#000"
                            },
                            "keyword4": {
                                "value": time_,
                                "color": "#000"
                            },
                            "remark": {
                                "value": "请于{}以内完全此学习任务。".format(limit),
                                "color": "#000"
                            },

                        }
                    }
                    json_data = json.dumps(msg)
                    url4 = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s' % access_token
                    r = requests.post(url4, json_data)
                    print(json.loads(r.text))
                else:
                    pass
            else:
                if user and user.openid:
                    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(
                        appid,
                        secret)
                    response = requests.get(url)
                    logger.info('post[%s]=>[%s][%s][%s]' % (
                        appid, secret, response.status_code, response.text
                    ))
                    resData = response.json()
                    access_token = resData['access_token']

                    u_openid = user.openid

                    url1 = 'https://api.weixin.qq.com/cgi-bin/template/get_all_private_template?access_token={}'.format(
                        access_token)
                    response = requests.get(url1)
                    logger.info('post[%s]=>[%s][%s]' % (
                        access_token, response.status_code, response.text
                    ))
                    resData = response.json()

                    openid = u_openid
                    template_id = resData['template_list'][-1]['template_id']
                    url = 'https://pocketstation.cn/'
                    time_ = datetime.datetime.now().strftime('%F %T')
                    msg = {
                        "touser": openid,
                        "template_id": template_id,
                        "url": url,
                        "data": {
                            "first": {
                                "value": "你有新的学习任务，请查收。",
                                "color": "#000"
                            },
                            "keyword1": {
                                "value": "口袋加油站",
                                "color": "#000"
                            },
                            "keyword2": {
                                "value": "无",
                                "color": "#000"
                            },
                            "keyword3": {
                                "value": lesson.name,
                                "color": "#000"
                            },
                            "keyword4": {
                                "value": time_,
                                "color": "#000"
                            },
                            "remark": {
                                "value": "请于{}以内完全此学习任务。".format(limit),
                                "color": "#000"
                            },

                        }
                    }
                    json_data = json.dumps(msg)
                    url4 = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s' % access_token
                    r = requests.post(url4, json_data)
                    print(json.loads(r.text))
                else:
                    pass
            traintask = TrainingTask()
            traintask.limit = limit
            traintask.lsn_id = lsn_id
            traintask.staff_id = staff_id
            db.session.add(traintask)
            db.session.commit()

            return jsonify({'msg':'添加成功！'})

class TrainTaskResource1(Resource):
    def delete(self,id):
        traintask = TrainingTask.query.filter(TrainingTask.id.__eq__(id)).first()
        if traintask:
            db.session.delete(traintask)
            db.session.commit()
            return jsonify({'msg':'删除成功！'})
        else:
            return jsonify({})

class LearnTask(Resource):
    def get(self,staff_id):
        list_ = []
        learns = TrainingTask.query.filter(TrainingTask.staff_id==staff_id).all()
        staff = User.query.filter(User.id==staff_id).first()
        if staff:
            lesson_ = {
                'lesson':staff.lesson_
            }
        else:
            pass
        if learns:
            for learn in learns:
                lessons = Lesson.query.filter(Lesson.id==learn.lsn_id).all()
                if lessons:
                    for lesson in lessons:
                        data = {
                            'id':learn.id,
                            'create_at':learn.create_at.strftime('%Y/%m/%d'),
                            'limit':learn.limit,
                            'finish_at':learn.finish_at.strftime('%Y/%m/%d'),
                            'now':datetime.datetime.now().strftime('%Y/%m/%d'),
                            'lsn':{
                                'id':lesson.id,
                                'name':lesson.name
                            }
                        }
                        list_.append(data)
            return jsonify(list_,lesson_)
        else:
            return jsonify([])


#员工学习课程记录
class LearnTask1(Resource):
    def get(self,staff_id,lsn_id):
        year_ = datetime.datetime.now().year
        month_ = datetime.datetime.now().month
        day_ = datetime.datetime.now().day
        user_ = User.query.filter(User.id == staff_id, and_(
            extract('year', User.update_time) == year_,
            extract('month', User.update_time) == month_,
            extract('day', User.update_time) == day_
        )).first()

        staff = User.query.filter(User.id==staff_id).first()
        if staff.lesson_:
            str1 = staff.lesson_ + '#' + lsn_id
            str2 = str1.split('#')
            str3 = list(set(str2))
            staff.lesson_ = "#".join(str3)
            staff.lesson_dayno = "#".join(str3)
            db.session.commit()

            if user_:
                pass
            else:
                u = User.query.filter(User.id == staff_id).first()
                u.lesson_dayno = lsn_id
                db.session.commit()

            return jsonify({'msg':'成功'})
        else:
            staff.lesson_ = lsn_id
            staff.lesson_dayno = lsn_id
            db.session.commit()
            return jsonify({'msg': '成功'})


