import datetime
import json

from flask import jsonify
from flask_restful import Resource, reqparse
import requests

from App.apis.TokenApi import logger
from App.models import Lesson, LessonClas, Operation, db, User, Position, BusinessUnit, LessonPermission, \
    Tool, LessonThumb, LessonCollection, Admin, Question

parser = reqparse.RequestParser()
parser.add_argument(name='name', type=str)
parser.add_argument(name='oprt_id', type=int)
parser.add_argument(name='img_src', type=str)
parser.add_argument(name='type', type=str)
parser.add_argument(name='contents', type=str)
parser.add_argument(name='lecturer_id', type=int)
parser.add_argument(name='is_look', type=int)
parser.add_argument(name='recommended', type=int)
parser.add_argument(name='permissions', type=str)

class LessonResource(Resource):
    def get(self):
        lessons = Lesson.query.all()
        list_ = []
        for lesson in lessons:
            if lesson.lecturer_id:
                user = User.query.filter(User.id.__eq__(lesson.lecturer_id)).first()
                pos = Position.query.filter(Position.id.__eq__(user.pos_id)).first()
                oper = Operation.query.filter(Operation.id.__eq__(lesson.oper_id)).first()
                les_cls = LessonClas.query.filter(LessonClas.id.__eq__(oper.cls_id)).first()
                permissions = LessonPermission.query.filter(LessonPermission.lsn_id.__eq__(lesson.id)).all()
                if permissions != None:
                    for perm in permissions:
                        bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(perm.bu_id)).first()
                        data = {
                            'id':lesson.id,
                            'name':lesson.name,
                            'type':lesson.type,
                            'recommended':lesson.recommended,
                            'is_look': lesson.is_look,
                            'img_src':lesson.img_src,
                            'content':lesson.content,
                            "be_thumbs": [],
                            "tags": [],
                            "lecturer":{
                                'id':user.id,
                                'name':user.name,
                                'avatar':user.img_src,
                                'lessons':[],
                                'pos':{
                                    'id':pos.id,
                                    'name':pos.name,
                                    # 'bu':{
                                    #     'id':bu.id,
                                    #     'name':bu.name
                                    # }
                                }
                            },
                            'oprt':{
                                'id':oper.id,
                                'name':oper.name,
                                'cls': {
                                    'id': les_cls.id,
                                    'name': les_cls.name
                                },
                            },
                            "lesson_permissions": {
                                'name': lesson.name,
                                "bu": {
                                    "name": bu.name,
                                    "id":bu.id,
                                },
                            }
                        }
                        list_.append(data)
            else:
                oper = Operation.query.filter(Operation.id.__eq__(lesson.oper_id)).first()
                les_cls = LessonClas.query.filter(LessonClas.id.__eq__(oper.cls_id)).first()
                permissions = LessonPermission.query.filter(LessonPermission.lsn_id.__eq__(lesson.id)).all()
                if permissions != None:
                    for perm in permissions:
                        bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(perm.bu_id)).first()
                        data = {
                            'id': lesson.id,
                            'name': lesson.name,
                            'type': lesson.type,
                            'recommended': lesson.recommended,
                            'is_look': lesson.is_look,
                            'img_src': lesson.img_src,
                            'content': lesson.content,
                            "be_thumbs": [],
                            "tags": [],
                            "lecturer": {
                            },
                            'oprt': {
                                'id': oper.id,
                                'name': oper.name,
                                'cls': {
                                    'id': les_cls.id,
                                    'name': les_cls.name
                                },
                            },
                            "lesson_permissions": {
                                'name': lesson.name,
                                "bu": {
                                    "name": bu.name,
                                    "id": bu.id,
                                },
                            }
                        }
                        list_.append(data)
            list2 = []
            for i in range(len(list_)):
                if list_[i] != {}:
                    order_list = []
                    order_list.append(list_[i].get('lesson_permissions'))
                    for j in range(i + 1, len(list_)):
                        if list_[i].get('name') == list_[j].get('name'):
                            order_list.append(list_[j].get('lesson_permissions'))
                            list_[i]['lesson_permissions'] = order_list
                            list_[j] = {}
                    if type(list_[i]['lesson_permissions']) == list:
                        pass
                    else:
                        list_[i]['lesson_permissions'] = [list_[i]['lesson_permissions']]
                    list2.append(list_[i])
        return jsonify(list2)

    def post(self):
        parse = parser.parse_args()
        name = parse.get('name')
        oper_id = parse.get('oprt_id')
        img_src = parse.get('img_src')
        type = parse.get('type')
        content = parse.get('contents')
        recommended = parse.get('recommended')
        is_look = parse.get('is_look')
        lecturer_id = parse.get('lecturer_id')
        permissions = parse.get('permissions')
        permissions = eval(permissions)
        print(permissions)
        for keys,vals in permissions.items():
            bu_id = vals['bu_id']
            pos = Position.query.filter(Position.bu_id==bu_id).first()
            if pos:
                user = User.query.filter(User.pos_id==pos.id).first()
                if user and user.openid:
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

                    u_openid = user.openid

                    url1 = 'https://api.weixin.qq.com/cgi-bin/template/get_all_private_template?access_token={}'.format(
                        access_token)
                    response = requests.get(url1)
                    logger.info('post[%s]=>[%s][%s]' % (
                        access_token, response.status_code, response.text
                    ))
                    resData = response.json()

                    openid = u_openid
                    template_id = resData['template_list'][-2]['template_id']
                    url = 'http://192.168.1.104：8000/'

                    year = datetime.datetime.now().year
                    month = datetime.datetime.now().month
                    day = datetime.datetime.now().day
                    msg = {
                        "touser": openid,
                        "template_id": template_id,
                        "url": url,
                        "data": {
                            "userName": {
                                "value": user.name,
                                "color": "#000"
                            },
                            "courseName": {
                                "value": name,
                                "color": "#000"
                            },
                            "date": {
                                "value": str(year) + "年" + str(month) + "月"+ str(day),
                                "color": "#000"
                            },
                            # "remark": {
                            #     "value": "想了解师资详情，可回复2",
                            #     "color": "#000"
                            # },
                            # "remark": {
                            #     "value": "想了解更多课程，可回复3",
                            #     "color": "#000"
                            # },
                            "remark": {
                                "value": "感谢您对口袋加油站的支持。",
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
                pass

        lesson = Lesson()
        lesson.name = name
        lesson.oper_id = oper_id
        lesson.img_src = img_src
        lesson.type = type
        lesson.content = content
        lesson.is_look = is_look
        lesson.recommended = recommended
        lesson.lecturer_id = lecturer_id
        try:
            db.session.add(lesson)
            db.session.commit()
        except Exception as e:
            print(str(e))
        for vals in permissions.values():
            lessons = Lesson.query.filter(Lesson.name.__eq__(name)).first()
            permission = LessonPermission()
            permission.lsn_id = lessons.id
            permission.bu_id = vals['bu_id']
            permission.need_manager = vals['need_manager']
            db.session.add(permission)
            db.session.commit()

        return jsonify({'msg':'添加成功！'})

class LessonResource1(Resource):
    def get(self,id,staff_id):
        if staff_id != 'dealer':
            lessons = []
            u = User.query.filter(User.id==staff_id).first()
            lesson = Lesson.query.filter(Lesson.id.__eq__(id)).first()
            ques = Question.query.filter(Question.lsn_id == lesson.id).first()
            oper = Operation.query.filter(Operation.id.__eq__(lesson.oper_id)).first()
            lescls = LessonClas.query.filter(LessonClas.id.__eq__(oper.cls_id)).first()
            if lesson.lecturer_id:
                lessonses = Lesson.query.filter(Lesson.lecturer_id.__eq__(lesson.lecturer_id)).all()
                for les in lessonses:
                    lessons.append(les.id)
                user = User.query.filter(User.id.__eq__(lesson.lecturer_id)).first()
                pos = Position.query.filter(Position.id.__eq__(user.pos_id)).first()
                bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos.bu_id)).first()
                les_permissions = LessonPermission.query.filter(LessonPermission.lsn_id.__eq__(lesson.id)).all()
                for les_permission in les_permissions:
                    bu1 = BusinessUnit.query.filter(BusinessUnit.id.__eq__(les_permission.bu_id)).first()
                    be_thumbs = []
                    be_collected = []
                    thumbs = LessonThumb.query.filter(LessonThumb.lsn_id.__eq__(id)).all()
                    for thumb in thumbs:
                        be_thumbs.append(thumb.staff_id)
                    lsn_collects = LessonCollection.query.filter(LessonCollection.lesson_id.__eq__(id)).all()
                    for lsn_collect in lsn_collects:
                        be_collected.append(lsn_collect.staff_id)
                    tools = Tool.query.filter(Tool.lsn_id.__eq__(lesson.id)).all()
                    if tools:
                        for tool in tools:
                            if ques:
                                data = {
                                    "be_thumbs": be_thumbs,
                                    "img_src": lesson.img_src,
                                    'tags': [],
                                    "lecturer": {
                                        'name': user.name,
                                        'avatar': user.img_src,
                                        'lessons': lessons,
                                        'pos': {
                                            'id': pos.id,
                                            'name': pos.name,
                                            'bu': {
                                                'name': bu.name,
                                                'id': bu.id
                                            },
                                        }
                                    },
                                    'oprt': {
                                        'id': oper.id,
                                        'name': oper.name,
                                        'cls': {
                                            'id': lescls.id,
                                            'name': lescls.name
                                        }
                                    },
                                    'contents': [lesson.content],
                                    'id': lesson.id,
                                    'name': lesson.name,
                                    'be_collected': be_collected,
                                    'type': lesson.type,
                                    'tools': {
                                        'name': tool.name,
                                        'type': tool.type,
                                        'id': tool.id,
                                        'content': tool.content
                                    },
                                    'passed': u.passed,
                                    'test': True,
                                    'create_at': lesson.create_at,
                                    'lesson_permissions': {
                                        'bu': {
                                            'name': bu1.name,
                                            'id': bu1.id
                                        },
                                        "need_manager": 0,
                                        'id': les_permission.id
                                    },
                                }
                                return jsonify(data)
                            else:
                                data = {
                                    "be_thumbs": be_thumbs,
                                    "img_src": lesson.img_src,
                                    'tags': [],
                                    "lecturer": {
                                        'name': user.name,
                                        'avatar': user.img_src,
                                        'lessons': lessons,
                                        'pos': {
                                            'id': pos.id,
                                            'name': pos.name,
                                            'bu': {
                                                'name': bu.name,
                                                'id': bu.id
                                            },
                                        }
                                    },
                                    'oprt': {
                                        'id': oper.id,
                                        'name': oper.name,
                                        'cls': {
                                            'id': lescls.id,
                                            'name': lescls.name
                                        }
                                    },
                                    'contents': [lesson.content],
                                    'id': lesson.id,
                                    'name': lesson.name,
                                    'be_collected': be_collected,
                                    'type': lesson.type,
                                    'tools': {
                                        'name': tool.name,
                                        'type': tool.type,
                                        'id': tool.id,
                                        'content': tool.content
                                    },
                                    'passed': u.passed,
                                    'test': False,
                                    'create_at': lesson.create_at,
                                    'lesson_permissions': {
                                        'bu': {
                                            'name': bu1.name,
                                            'id': bu1.id
                                        },
                                        "need_manager": 0,
                                        'id': les_permission.id
                                    },
                                }
                                return jsonify(data)
                    elif staff_id == 'dealer':
                        if ques:
                            data = {
                                "be_thumbs": be_thumbs,
                                "img_src": lesson.img_src,
                                'tags': [],
                                "lecturer": {
                                    'name': user.name,
                                    'avatar': user.img_src,
                                    'lessons': lessons,
                                    'pos': {
                                        'id': pos.id,
                                        'name': pos.name,
                                        'bu': {
                                            'name': bu.name,
                                            'id': bu.id
                                        },
                                    }
                                },
                                'oprt': {
                                    'id': oper.id,
                                    'name': oper.name,
                                    'cls': {
                                        'id': lescls.id,
                                        'name': lescls.name
                                    }
                                },
                                'contents': [lesson.content],
                                'id': lesson.id,
                                'name': lesson.name,
                                'be_collected': be_collected,
                                'type': lesson.type,
                                'tools': [],
                                'passed': u.passed,
                                'test': True,
                                'create_at': lesson.create_at,
                                'lesson_permissions': {
                                    'bu': {
                                        'name': bu1.name,
                                        'id': bu1.id
                                    },
                                    "need_manager": 0,
                                    'id': les_permission.id
                                },
                            }
                            return jsonify(data)
                        else:
                            data = {
                                "be_thumbs": be_thumbs,
                                "img_src": lesson.img_src,
                                'tags': [],
                                "lecturer": {
                                    'name': user.name,
                                    'avatar': user.img_src,
                                    'lessons': lessons,
                                    'pos': {
                                        'id': pos.id,
                                        'name': pos.name,
                                        'bu': {
                                            'name': bu.name,
                                            'id': bu.id
                                        },
                                    }
                                },
                                'oprt': {
                                    'id': oper.id,
                                    'name': oper.name,
                                    'cls': {
                                        'id': lescls.id,
                                        'name': lescls.name
                                    }
                                },
                                'contents': [lesson.content],
                                'id': lesson.id,
                                'name': lesson.name,
                                'be_collected': be_collected,
                                'type': lesson.type,
                                'tools': [],
                                'passed': u.passed,
                                'test': False,
                                'create_at': lesson.create_at,
                                'lesson_permissions': {
                                    'bu': {
                                        'name': bu1.name,
                                        'id': bu1.id
                                    },
                                    "need_manager": 0,
                                    'id': les_permission.id
                                },
                            }
                            return jsonify(data)
                    else:
                        pass
            else:
                les_permissions = LessonPermission.query.filter(LessonPermission.lsn_id.__eq__(lesson.id)).all()
                for les_permission in les_permissions:
                    bu1 = BusinessUnit.query.filter(BusinessUnit.id.__eq__(les_permission.bu_id)).first()
                    be_thumbs = []
                    be_collected = []
                    thumbs = LessonThumb.query.filter(LessonThumb.lsn_id.__eq__(id)).all()
                    for thumb in thumbs:
                        be_thumbs.append(thumb.staff_id)
                    lsn_collects = LessonCollection.query.filter(LessonCollection.lesson_id.__eq__(id)).all()
                    for lsn_collect in lsn_collects:
                        be_collected.append(lsn_collect.staff_id)
                    tools = Tool.query.filter(Tool.lsn_id.__eq__(lesson.id)).all()
                    if tools:
                        for tool in tools:
                            if ques:
                                data = {
                                    "be_thumbs": be_thumbs,
                                    "img_src": lesson.img_src,
                                    'tags': [],
                                    "lecturer": {},
                                    'oprt': {
                                        'id': oper.id,
                                        'name': oper.name,
                                        'cls': {
                                            'id': lescls.id,
                                            'name': lescls.name
                                        }
                                    },
                                    'contents': lesson.content,
                                    'id': lesson.id,
                                    'name': lesson.name,
                                    'be_collected': be_collected,
                                    'type': lesson.type,
                                    'tools': {
                                        'name': tool.name,
                                        'type': tool.type,
                                        'id': tool.id,
                                        'content': tool.content
                                    },
                                    'passed': u.passed,
                                    'test': True,
                                    'create_at': lesson.create_at,
                                    'lesson_permissions': {
                                        'bu': {
                                            'name': bu1.name,
                                            'id': bu1.id
                                        },
                                        "need_manager": 0,
                                        'id': les_permission.id
                                    },
                                }
                                return jsonify(data)
                            else:
                                data = {
                                    "be_thumbs": be_thumbs,
                                    "img_src": lesson.img_src,
                                    'tags': [],
                                    "lecturer": {},
                                    'oprt': {
                                        'id': oper.id,
                                        'name': oper.name,
                                        'cls': {
                                            'id': lescls.id,
                                            'name': lescls.name
                                        }
                                    },
                                    'contents': lesson.content,
                                    'id': lesson.id,
                                    'name': lesson.name,
                                    'be_collected': be_collected,
                                    'type': lesson.type,
                                    'tools': {
                                        'name': tool.name,
                                        'type': tool.type,
                                        'id': tool.id,
                                        'content': tool.content
                                    },
                                    'passed': u.passed,
                                    'test': False,
                                    'create_at': lesson.create_at,
                                    'lesson_permissions': {
                                        'bu': {
                                            'name': bu1.name,
                                            'id': bu1.id
                                        },
                                        "need_manager": 0,
                                        'id': les_permission.id
                                    },
                                }
                                return jsonify(data)
                    else:
                        if ques:
                            data = {
                                "be_thumbs": be_thumbs,
                                "img_src": lesson.img_src,
                                'tags': [],
                                "lecturer": {},
                                'oprt': {
                                    'id': oper.id,
                                    'name': oper.name,
                                    'cls': {
                                        'id': lescls.id,
                                        'name': lescls.name
                                    }
                                },
                                'contents': lesson.content,
                                'id': lesson.id,
                                'name': lesson.name,
                                'be_collected': be_collected,
                                'type': lesson.type,
                                'tools': [],
                                'passed': u.passed,
                                'test': True,
                                'create_at': lesson.create_at,
                                'lesson_permissions': {
                                    'bu': {
                                        'name': bu1.name,
                                        'id': bu1.id
                                    },
                                    "need_manager": 0,
                                    'id': les_permission.id
                                },
                            }
                            return jsonify(data)
                        else:
                            data = {
                                "be_thumbs": be_thumbs,
                                "img_src": lesson.img_src,
                                'tags': [],
                                "lecturer": {},
                                'oprt': {
                                    'id': oper.id,
                                    'name': oper.name,
                                    'cls': {
                                        'id': lescls.id,
                                        'name': lescls.name
                                    }
                                },
                                'contents': lesson.content,
                                'id': lesson.id,
                                'name': lesson.name,
                                'be_collected': be_collected,
                                'type': lesson.type,
                                'tools': [],
                                'passed': u.passed,
                                'test': False,
                                'create_at': lesson.create_at,
                                'lesson_permissions': {
                                    'bu': {
                                        'name': bu1.name,
                                        'id': bu1.id
                                    },
                                    "need_manager": 0,
                                    'id': les_permission.id
                                },
                            }
                            return jsonify(data)
        else:
            lessons = []
            lesson = Lesson.query.filter(Lesson.id.__eq__(id)).first()
            ques = Question.query.filter(Question.lsn_id == lesson.id).first()
            oper = Operation.query.filter(Operation.id.__eq__(lesson.oper_id)).first()
            lescls = LessonClas.query.filter(LessonClas.id.__eq__(oper.cls_id)).first()
            if lesson.lecturer_id:
                lessonses = Lesson.query.filter(Lesson.lecturer_id.__eq__(lesson.lecturer_id)).all()
                for les in lessonses:
                    lessons.append(les.id)
                user = User.query.filter(User.id.__eq__(lesson.lecturer_id)).first()
                pos = Position.query.filter(Position.id.__eq__(user.pos_id)).first()
                bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos.bu_id)).first()
                les_permissions = LessonPermission.query.filter(LessonPermission.lsn_id.__eq__(lesson.id)).all()
                for les_permission in les_permissions:
                    bu1 = BusinessUnit.query.filter(BusinessUnit.id.__eq__(les_permission.bu_id)).first()
                    be_thumbs = []
                    be_collected = []
                    thumbs = LessonThumb.query.filter(LessonThumb.lsn_id.__eq__(id)).all()
                    for thumb in thumbs:
                        be_thumbs.append(thumb.staff_id)
                    lsn_collects = LessonCollection.query.filter(LessonCollection.lesson_id.__eq__(id)).all()
                    for lsn_collect in lsn_collects:
                        be_collected.append(lsn_collect.staff_id)
                    tools = Tool.query.filter(Tool.lsn_id.__eq__(lesson.id)).all()
                    if tools:
                        for tool in tools:
                            if ques:
                                data = {
                                    "be_thumbs": be_thumbs,
                                    "img_src": lesson.img_src,
                                    'tags': [],
                                    "lecturer": {
                                        'name': user.name,
                                        'avatar': user.img_src,
                                        'lessons': lessons,
                                        'pos': {
                                            'id': pos.id,
                                            'name': pos.name,
                                            'bu': {
                                                'name': bu.name,
                                                'id': bu.id
                                            },
                                        }
                                    },
                                    'oprt': {
                                        'id': oper.id,
                                        'name': oper.name,
                                        'cls': {
                                            'id': lescls.id,
                                            'name': lescls.name
                                        }
                                    },
                                    'contents': [lesson.content],
                                    'id': lesson.id,
                                    'name': lesson.name,
                                    'be_collected': be_collected,
                                    'type': lesson.type,
                                    'tools': {
                                        'name': tool.name,
                                        'type': tool.type,
                                        'id': tool.id,
                                        'content': tool.content
                                    },
                                    'passed': False,
                                    'test': True,
                                    'create_at': lesson.create_at,
                                    'lesson_permissions': {
                                        'bu': {
                                            'name': bu1.name,
                                            'id': bu1.id
                                        },
                                        "need_manager": 0,
                                        'id': les_permission.id
                                    },
                                }
                                return jsonify(data)
                            else:
                                data = {
                                    "be_thumbs": be_thumbs,
                                    "img_src": lesson.img_src,
                                    'tags': [],
                                    "lecturer": {
                                        'name': user.name,
                                        'avatar': user.img_src,
                                        'lessons': lessons,
                                        'pos': {
                                            'id': pos.id,
                                            'name': pos.name,
                                            'bu': {
                                                'name': bu.name,
                                                'id': bu.id
                                            },
                                        }
                                    },
                                    'oprt': {
                                        'id': oper.id,
                                        'name': oper.name,
                                        'cls': {
                                            'id': lescls.id,
                                            'name': lescls.name
                                        }
                                    },
                                    'contents': [lesson.content],
                                    'id': lesson.id,
                                    'name': lesson.name,
                                    'be_collected': be_collected,
                                    'type': lesson.type,
                                    'tools': {
                                        'name': tool.name,
                                        'type': tool.type,
                                        'id': tool.id,
                                        'content': tool.content
                                    },
                                    'passed': False,
                                    'test': False,
                                    'create_at': lesson.create_at,
                                    'lesson_permissions': {
                                        'bu': {
                                            'name': bu1.name,
                                            'id': bu1.id
                                        },
                                        "need_manager": 0,
                                        'id': les_permission.id
                                    },
                                }
                                return jsonify(data)
                    else:
                        if ques:
                            data = {
                                "be_thumbs": be_thumbs,
                                "img_src": lesson.img_src,
                                'tags': [],
                                "lecturer": {
                                    'name': user.name,
                                    'avatar': user.img_src,
                                    'lessons': lessons,
                                    'pos': {
                                        'id': pos.id,
                                        'name': pos.name,
                                        'bu': {
                                            'name': bu.name,
                                            'id': bu.id
                                        },
                                    }
                                },
                                'oprt': {
                                    'id': oper.id,
                                    'name': oper.name,
                                    'cls': {
                                        'id': lescls.id,
                                        'name': lescls.name
                                    }
                                },
                                'contents': [lesson.content],
                                'id': lesson.id,
                                'name': lesson.name,
                                'be_collected': be_collected,
                                'type': lesson.type,
                                'tools': [],
                                'passed': False,
                                'test': True,
                                'create_at': lesson.create_at,
                                'lesson_permissions': {
                                    'bu': {
                                        'name': bu1.name,
                                        'id': bu1.id
                                    },
                                    "need_manager": 0,
                                    'id': les_permission.id
                                },
                            }
                            return jsonify(data)
                        else:
                            data = {
                                "be_thumbs": be_thumbs,
                                "img_src": lesson.img_src,
                                'tags': [],
                                "lecturer": {
                                    'name': user.name,
                                    'avatar': user.img_src,
                                    'lessons': lessons,
                                    'pos': {
                                        'id': pos.id,
                                        'name': pos.name,
                                        'bu': {
                                            'name': bu.name,
                                            'id': bu.id
                                        },
                                    }
                                },
                                'oprt': {
                                    'id': oper.id,
                                    'name': oper.name,
                                    'cls': {
                                        'id': lescls.id,
                                        'name': lescls.name
                                    }
                                },
                                'contents': [lesson.content],
                                'id': lesson.id,
                                'name': lesson.name,
                                'be_collected': be_collected,
                                'type': lesson.type,
                                'tools': [],
                                'passed': False,
                                'test': False,
                                'create_at': lesson.create_at,
                                'lesson_permissions': {
                                    'bu': {
                                        'name': bu1.name,
                                        'id': bu1.id
                                    },
                                    "need_manager": 0,
                                    'id': les_permission.id
                                },
                            }
                            return jsonify(data)
            else:
                les_permissions = LessonPermission.query.filter(LessonPermission.lsn_id.__eq__(lesson.id)).all()
                for les_permission in les_permissions:
                    bu1 = BusinessUnit.query.filter(BusinessUnit.id.__eq__(les_permission.bu_id)).first()
                    be_thumbs = []
                    be_collected = []
                    thumbs = LessonThumb.query.filter(LessonThumb.lsn_id.__eq__(id)).all()
                    for thumb in thumbs:
                        be_thumbs.append(thumb.staff_id)
                    lsn_collects = LessonCollection.query.filter(LessonCollection.lesson_id.__eq__(id)).all()
                    for lsn_collect in lsn_collects:
                        be_collected.append(lsn_collect.staff_id)
                    tools = Tool.query.filter(Tool.lsn_id.__eq__(lesson.id)).all()
                    if tools:
                        for tool in tools:
                            if ques:
                                data = {
                                    "be_thumbs": be_thumbs,
                                    "img_src": lesson.img_src,
                                    'tags': [],
                                    "lecturer": {},
                                    'oprt': {
                                        'id': oper.id,
                                        'name': oper.name,
                                        'cls': {
                                            'id': lescls.id,
                                            'name': lescls.name
                                        }
                                    },
                                    'contents': lesson.content,
                                    'id': lesson.id,
                                    'name': lesson.name,
                                    'be_collected': be_collected,
                                    'type': lesson.type,
                                    'tools': {
                                        'name': tool.name,
                                        'type': tool.type,
                                        'id': tool.id,
                                        'content': tool.content
                                    },
                                    'passed': False,
                                    'test': True,
                                    'create_at': lesson.create_at,
                                    'lesson_permissions': {
                                        'bu': {
                                            'name': bu1.name,
                                            'id': bu1.id
                                        },
                                        "need_manager": 0,
                                        'id': les_permission.id
                                    },
                                }
                                return jsonify(data)
                            else:
                                data = {
                                    "be_thumbs": be_thumbs,
                                    "img_src": lesson.img_src,
                                    'tags': [],
                                    "lecturer": {},
                                    'oprt': {
                                        'id': oper.id,
                                        'name': oper.name,
                                        'cls': {
                                            'id': lescls.id,
                                            'name': lescls.name
                                        }
                                    },
                                    'contents': lesson.content,
                                    'id': lesson.id,
                                    'name': lesson.name,
                                    'be_collected': be_collected,
                                    'type': lesson.type,
                                    'tools': {
                                        'name': tool.name,
                                        'type': tool.type,
                                        'id': tool.id,
                                        'content': tool.content
                                    },
                                    'passed': False,
                                    'test': False,
                                    'create_at': lesson.create_at,
                                    'lesson_permissions': {
                                        'bu': {
                                            'name': bu1.name,
                                            'id': bu1.id
                                        },
                                        "need_manager": 0,
                                        'id': les_permission.id
                                    },
                                }
                                return jsonify(data)
                    else:
                        if ques:
                            data = {
                                "be_thumbs": be_thumbs,
                                "img_src": lesson.img_src,
                                'tags': [],
                                "lecturer": {},
                                'oprt': {
                                    'id': oper.id,
                                    'name': oper.name,
                                    'cls': {
                                        'id': lescls.id,
                                        'name': lescls.name
                                    }
                                },
                                'contents': lesson.content,
                                'id': lesson.id,
                                'name': lesson.name,
                                'be_collected': be_collected,
                                'type': lesson.type,
                                'tools': [],
                                'passed': False,
                                'test': True,
                                'create_at': lesson.create_at,
                                'lesson_permissions': {
                                    'bu': {
                                        'name': bu1.name,
                                        'id': bu1.id
                                    },
                                    "need_manager": 0,
                                    'id': les_permission.id
                                },
                            }
                            return jsonify(data)
                        else:
                            data = {
                                "be_thumbs": be_thumbs,
                                "img_src": lesson.img_src,
                                'tags': [],
                                "lecturer": {},
                                'oprt': {
                                    'id': oper.id,
                                    'name': oper.name,
                                    'cls': {
                                        'id': lescls.id,
                                        'name': lescls.name
                                    }
                                },
                                'contents': lesson.content,
                                'id': lesson.id,
                                'name': lesson.name,
                                'be_collected': be_collected,
                                'type': lesson.type,
                                'tools': [],
                                'passed': False,
                                'test': False,
                                'create_at': lesson.create_at,
                                'lesson_permissions': {
                                    'bu': {
                                        'name': bu1.name,
                                        'id': bu1.id
                                    },
                                    "need_manager": 0,
                                    'id': les_permission.id
                                },
                            }
                            return jsonify(data)

    def post(self,id):
        parser = reqparse.RequestParser()
        parser.add_argument(name='recommended', type=int)
        parse = parser.parse_args()
        recommended = parse.get('recommended')
        lsn = Lesson.query.filter(Lesson.id.__eq__(id)).first()
        if lsn:
            lsn.recommended = recommended
            db.session.commit()
            return jsonify({'msg': '设置成功！'})
        else:
            return jsonify({'err': '暂无信息！'})

    def put(self,id):
        parse = parser.parse_args()
        name = parse.get('name')
        img_src = parse.get('img_src')
        lesson = Lesson.query.filter(Lesson.id.__eq__(id)).first()
        if lesson:
            lesson.name = name
            lesson.img_src = img_src
            db.session.commit()
            return jsonify({'msg':'修改成功！'})
        else:
            return jsonify({})

    def delete(self,id):
        lesson = Lesson.query.filter(Lesson.id.__eq__(id)).first()
        if lesson:
            db.session.delete(lesson)
            db.session.commit()
            return jsonify({'msg':'删除成功！'})
        else:
            return jsonify({'err':404})

class LessonResource2(Resource):
    def get(self,subPart_id,openid,types):
        if types == 'staff':
            list_ = []
            user = User.query.filter(User.openid.__eq__(openid)).first()
            pos = Position.query.filter(Position.id.__eq__(user.pos_id)).first()
            bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos.bu_id)).first()
            if bu:
                les_permissions = LessonPermission.query.filter(LessonPermission.bu_id.__eq__(bu.id)).all()
                if les_permissions:
                    for les_permission in les_permissions:
                        bu2 = BusinessUnit.query.filter(BusinessUnit.id.__eq__(les_permission.bu_id)).first()
                        lessons = Lesson.query.filter(Lesson.oper_id.__eq__(subPart_id),Lesson.id.__eq__(les_permission.lsn_id)).all()
                        for lesson in lessons:
                            ques = Question.query.filter(Question.lsn_id == lesson.id).first()
                            if lesson.lecturer_id:
                                oper = Operation.query.filter(Operation.id.__eq__(lesson.oper_id)).first()
                                lescls = LessonClas.query.filter(LessonClas.id.__eq__(oper.cls_id)).first()
                                staff = User.query.filter(User.id.__eq__(lesson.lecturer_id)).first()
                                pos1 = Position.query.filter(Position.id.__eq__(staff.pos_id)).first()
                                bu1 = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos1.bu_id)).first()
                                tools = Tool.query.filter(Tool.lsn_id.__eq__(lesson.id)).all()
                                if tools:
                                    for tool in tools:
                                        if ques:
                                            data = {
                                                "img_src": lesson.img_src,
                                                'tags': [],
                                                "lecturer": {
                                                    'name': staff.name,
                                                    'avatar': staff.img_src,
                                                    'lessons': [],
                                                    'pos': {
                                                        'id': pos1.id,
                                                        'name': pos1.name,
                                                        'bu': {
                                                            'name': bu1.name,
                                                            'id': bu1.id
                                                        },
                                                    }
                                                },
                                                'oprt': {
                                                    'id': oper.id,
                                                    'name': oper.name,
                                                    'cls': {
                                                        'id': lescls.id,
                                                        'name': lescls.name
                                                    }
                                                },
                                                'contents': lesson.content,
                                                'id': lesson.id,
                                                'name': lesson.name,
                                                'type': lesson.type,
                                                'tools': {
                                                    'name': tool.name,
                                                    'type': tool.type,
                                                    'id': tool.id,
                                                    'content': tool.content
                                                },
                                                'passed': False,
                                                'test': True,
                                                'create_at': lesson.create_at,
                                                'lesson_permissions': {
                                                    'bu': {
                                                        'name': bu2.name,
                                                        'id': bu2.id
                                                    },
                                                    "need_manager": 0,
                                                    'id': les_permission.id
                                                },
                                            }
                                            list_.append(data)
                                        else:
                                            data = {
                                                "img_src": lesson.img_src,
                                                'tags': [],
                                                "lecturer": {
                                                    'name': staff.name,
                                                    'avatar': staff.img_src,
                                                    'lessons': [],
                                                    'pos': {
                                                        'id': pos1.id,
                                                        'name': pos1.name,
                                                        'bu': {
                                                            'name': bu1.name,
                                                            'id': bu1.id
                                                        },
                                                    }
                                                },
                                                'oprt': {
                                                    'id': oper.id,
                                                    'name': oper.name,
                                                    'cls': {
                                                        'id': lescls.id,
                                                        'name': lescls.name
                                                    }
                                                },
                                                'contents': lesson.content,
                                                'id': lesson.id,
                                                'name': lesson.name,
                                                'type': lesson.type,
                                                'tools': {
                                                    'name': tool.name,
                                                    'type': tool.type,
                                                    'id': tool.id,
                                                    'content': tool.content
                                                },
                                                'passed': False,
                                                'test': False,
                                                'create_at': lesson.create_at,
                                                'lesson_permissions': {
                                                    'bu': {
                                                        'name': bu2.name,
                                                        'id': bu2.id
                                                    },
                                                    "need_manager": 0,
                                                    'id': les_permission.id
                                                },
                                            }
                                            list_.append(data)
                                else:
                                    if ques:
                                        data = {
                                            "img_src": lesson.img_src,
                                            'tags': [],
                                            "lecturer": {
                                                'name': staff.name,
                                                'avatar': staff.img_src,
                                                'lessons': [],
                                                'pos': {
                                                    'id': pos1.id,
                                                    'name': pos1.name,
                                                    'bu': {
                                                        'name': bu1.name,
                                                        'id': bu1.id
                                                    },
                                                }
                                            },
                                            'oprt': {
                                                'id': oper.id,
                                                'name': oper.name,
                                                'cls': {
                                                    'id': lescls.id,
                                                    'name': lescls.name
                                                }
                                            },
                                            'contents': lesson.content,
                                            'id': lesson.id,
                                            'name': lesson.name,
                                            'type': lesson.type,
                                            'tools': [],
                                            'passed': False,
                                            'test': True,
                                            'create_at': lesson.create_at,
                                            'lesson_permissions': {
                                                'bu': {
                                                    'name': bu2.name,
                                                    'id': bu2.id
                                                },
                                                "need_manager": 0,
                                                'id': les_permission.id
                                            },
                                        }
                                        list_.append(data)
                                    else:
                                        data = {
                                            "img_src": lesson.img_src,
                                            'tags': [],
                                            "lecturer": {
                                                'name': staff.name,
                                                'avatar': staff.img_src,
                                                'lessons': [],
                                                'pos': {
                                                    'id': pos1.id,
                                                    'name': pos1.name,
                                                    'bu': {
                                                        'name': bu1.name,
                                                        'id': bu1.id
                                                    },
                                                }
                                            },
                                            'oprt': {
                                                'id': oper.id,
                                                'name': oper.name,
                                                'cls': {
                                                    'id': lescls.id,
                                                    'name': lescls.name
                                                }
                                            },
                                            'contents': lesson.content,
                                            'id': lesson.id,
                                            'name': lesson.name,
                                            'type': lesson.type,
                                            'tools': [],
                                            'passed': False,
                                            'test': False,
                                            'create_at': lesson.create_at,
                                            'lesson_permissions': {
                                                'bu': {
                                                    'name': bu2.name,
                                                    'id': bu2.id
                                                },
                                                "need_manager": 0,
                                                'id': les_permission.id
                                            },
                                        }
                                        list_.append(data)
                            else:
                                tools = Tool.query.filter(Tool.lsn_id.__eq__(lesson.id)).all()
                                if tools:
                                    for tool in tools:
                                        if ques:
                                            data = {
                                                "img_src": lesson.img_src,
                                                'tags': [],
                                                "lecturer": 'null',
                                                'contents': lesson.content,
                                                'id': lesson.id,
                                                'name': lesson.name,
                                                'type': lesson.type,
                                                'tools': {
                                                    'name': tool.name,
                                                    'type': tool.type,
                                                    'id': tool.id,
                                                    'content': tool.content
                                                },
                                                'passed': False,
                                                'test': True,
                                                'create_at': lesson.create_at,
                                                'lesson_permissions': {
                                                    'bu': {
                                                        'name': bu2.name,
                                                        'id': bu2.id
                                                    },
                                                    "need_manager": 0,
                                                    'id': les_permission.id
                                                },
                                            }
                                            list_.append(data)
                                        else:
                                            data = {
                                                "img_src": lesson.img_src,
                                                'tags': [],
                                                "lecturer": 'null',
                                                'contents': lesson.content,
                                                'id': lesson.id,
                                                'name': lesson.name,
                                                'type': lesson.type,
                                                'tools': {
                                                    'name': tool.name,
                                                    'type': tool.type,
                                                    'id': tool.id,
                                                    'content': tool.content
                                                },
                                                'passed': False,
                                                'test': False,
                                                'create_at': lesson.create_at,
                                                'lesson_permissions': {
                                                    'bu': {
                                                        'name': bu2.name,
                                                        'id': bu2.id
                                                    },
                                                    "need_manager": 0,
                                                    'id': les_permission.id
                                                },
                                            }
                                            list_.append(data)
                                else:
                                    if ques:
                                        data = {
                                            "img_src": lesson.img_src,
                                            'tags': [],
                                            "lecturer": 'null',
                                            'contents': lesson.content,
                                            'id': lesson.id,
                                            'name': lesson.name,
                                            'type': lesson.type,
                                            'tools': [],
                                            'passed': False,
                                            'test': True,
                                            'create_at': lesson.create_at,
                                            'lesson_permissions': {
                                                'bu': {
                                                    'name': bu2.name,
                                                    'id': bu2.id
                                                },
                                                "need_manager": 0,
                                                'id': les_permission.id
                                            },
                                        }
                                        list_.append(data)
                                    else:
                                        data = {
                                            "img_src": lesson.img_src,
                                            'tags': [],
                                            "lecturer": 'null',
                                            'contents': lesson.content,
                                            'id': lesson.id,
                                            'name': lesson.name,
                                            'type': lesson.type,
                                            'tools': [],
                                            'passed': False,
                                            'test': False,
                                            'create_at': lesson.create_at,
                                            'lesson_permissions': {
                                                'bu': {
                                                    'name': bu2.name,
                                                    'id': bu2.id
                                                },
                                                "need_manager": 0,
                                                'id': les_permission.id
                                            },
                                        }
                                        list_.append(data)
                    list2 = []
                    for i in range(len(list_)):
                        if list_[i] != {}:
                            re_list = []
                            re_list.append(list_[i].get('tools'))
                            for j in range(i + 1, len(list_)):
                                if list_[i].get('id') == list_[j].get('id'):
                                    re_list.append(list_[j].get('tools'))
                                    list_[i]['tools'] = re_list
                                    list_[j] = {}
                            if type(list_[i]['tools']) == list:
                                pass
                            else:
                                list_[i]['tools'] = [list_[i]['tools']]
                            list2.append(list_[i])
                    return jsonify(list2)
                else:
                    return jsonify([])
            else:
                return jsonify([])

        elif types == 'dealer':
            list_ = []
            admin = Admin.query.filter(Admin.openid.__eq__(openid)).first()
            user = User.query.filter(User.openid.__eq__(openid)).first()
            if admin:
                les_permissions = LessonPermission.query.filter(LessonPermission.bu_id.__eq__(admin.bu_id)).all()
                for les_permission in les_permissions:
                    bu2 = BusinessUnit.query.filter(BusinessUnit.id.__eq__(les_permission.bu_id)).first()
                    lessons = Lesson.query.filter(Lesson.oper_id.__eq__(subPart_id),Lesson.id.__eq__(les_permission.lsn_id)).all()
                    for lesson in lessons:
                        ques = Question.query.filter(Question.lsn_id == lesson.id).first()
                        if lesson.is_look == 1:
                            if lesson.lecturer_id:
                                oper = Operation.query.filter(Operation.id.__eq__(lesson.oper_id)).first()
                                lescls = LessonClas.query.filter(LessonClas.id.__eq__(oper.cls_id)).first()
                                staff = User.query.filter(User.id.__eq__(lesson.lecturer_id)).first()
                                pos1 = Position.query.filter(Position.id.__eq__(staff.pos_id)).first()
                                bu1 = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos1.bu_id)).first()
                                tools = Tool.query.filter(Tool.lsn_id.__eq__(lesson.id)).all()
                                if tools:
                                    for tool in tools:
                                        if ques:
                                            data = {
                                                "img_src": lesson.img_src,
                                                'tags': [],
                                                "lecturer": {
                                                    'name': staff.name,
                                                    'avatar': staff.img_src,
                                                    'lessons': [],
                                                    'pos': {
                                                        'id': pos1.id,
                                                        'name': pos1.name,
                                                        'bu': {
                                                            'name': bu1.name,
                                                            'id': bu1.id
                                                        },
                                                    }
                                                },
                                                'oprt': {
                                                    'id': oper.id,
                                                    'name': oper.name,
                                                    'cls': {
                                                        'id': lescls.id,
                                                        'name': lescls.name
                                                    }
                                                },
                                                'contents': lesson.content,
                                                'id': lesson.id,
                                                'name': lesson.name,
                                                'type': lesson.type,
                                                'tools': {
                                                    'name': tool.name,
                                                    'type': tool.type,
                                                    'id': tool.id,
                                                    'content': tool.content
                                                },
                                                'passed': False,
                                                'test': True,
                                                'create_at': lesson.create_at,
                                                'lesson_permissions': {
                                                    'bu': {
                                                        'name': bu2.name,
                                                        'id': bu2.id
                                                    },
                                                    "need_manager": 0,
                                                    'id': les_permission.id
                                                },
                                            }
                                            list_.append(data)
                                        else:
                                            data = {
                                                "img_src": lesson.img_src,
                                                'tags': [],
                                                "lecturer": {
                                                    'name': staff.name,
                                                    'avatar': staff.img_src,
                                                    'lessons': [],
                                                    'pos': {
                                                        'id': pos1.id,
                                                        'name': pos1.name,
                                                        'bu': {
                                                            'name': bu1.name,
                                                            'id': bu1.id
                                                        },
                                                    }
                                                },
                                                'oprt': {
                                                    'id': oper.id,
                                                    'name': oper.name,
                                                    'cls': {
                                                        'id': lescls.id,
                                                        'name': lescls.name
                                                    }
                                                },
                                                'contents': lesson.content,
                                                'id': lesson.id,
                                                'name': lesson.name,
                                                'type': lesson.type,
                                                'tools': {
                                                    'name': tool.name,
                                                    'type': tool.type,
                                                    'id': tool.id,
                                                    'content': tool.content
                                                },
                                                'passed': False,
                                                'test': False,
                                                'create_at': lesson.create_at,
                                                'lesson_permissions': {
                                                    'bu': {
                                                        'name': bu2.name,
                                                        'id': bu2.id
                                                    },
                                                    "need_manager": 0,
                                                    'id': les_permission.id
                                                },
                                            }
                                            list_.append(data)
                                else:
                                    if ques:
                                        data = {
                                            "img_src": lesson.img_src,
                                            'tags': [],
                                            "lecturer": {
                                                'name': staff.name,
                                                'avatar': staff.img_src,
                                                'lessons': [],
                                                'pos': {
                                                    'id': pos1.id,
                                                    'name': pos1.name,
                                                    'bu': {
                                                        'name': bu1.name,
                                                        'id': bu1.id
                                                    },
                                                }
                                            },
                                            'oprt': {
                                                'id': oper.id,
                                                'name': oper.name,
                                                'cls': {
                                                    'id': lescls.id,
                                                    'name': lescls.name
                                                }
                                            },
                                            'contents': lesson.content,
                                            'id': lesson.id,
                                            'name': lesson.name,
                                            'type': lesson.type,
                                            'tools': [],
                                            'passed': False,
                                            'test': True,
                                            'create_at': lesson.create_at,
                                            'lesson_permissions': {
                                                'bu': {
                                                    'name': bu2.name,
                                                    'id': bu2.id
                                                },
                                                "need_manager": 0,
                                                'id': les_permission.id
                                            },
                                        }
                                        list_.append(data)
                                    else:
                                        data = {
                                            "img_src": lesson.img_src,
                                            'tags': [],
                                            "lecturer": {
                                                'name': staff.name,
                                                'avatar': staff.img_src,
                                                'lessons': [],
                                                'pos': {
                                                    'id': pos1.id,
                                                    'name': pos1.name,
                                                    'bu': {
                                                        'name': bu1.name,
                                                        'id': bu1.id
                                                    },
                                                }
                                            },
                                            'oprt': {
                                                'id': oper.id,
                                                'name': oper.name,
                                                'cls': {
                                                    'id': lescls.id,
                                                    'name': lescls.name
                                                }
                                            },
                                            'contents': lesson.content,
                                            'id': lesson.id,
                                            'name': lesson.name,
                                            'type': lesson.type,
                                            'tools': [],
                                            'passed': False,
                                            'test': True,
                                            'create_at': lesson.create_at,
                                            'lesson_permissions': {
                                                'bu': {
                                                    'name': bu2.name,
                                                    'id': bu2.id
                                                },
                                                "need_manager": 0,
                                                'id': les_permission.id
                                            },
                                        }
                                        list_.append(data)
                            else:
                                tools = Tool.query.filter(Tool.lsn_id.__eq__(lesson.id)).all()
                                if tools:
                                    for tool in tools:
                                        if ques:
                                            data = {
                                                "img_src": lesson.img_src,
                                                'tags': [],
                                                "lecturer": 'null',
                                                # 'oprt': {
                                                #     'id': oper.id,
                                                #     'name': oper.name,
                                                #     'cls': {
                                                #         'id': lescls.id,
                                                #         'name': lescls.name
                                                #     }
                                                # },
                                                'contents': lesson.content,
                                                'id': lesson.id,
                                                'name': lesson.name,
                                                'type': lesson.type,
                                                'tools': {
                                                    'name': tool.name,
                                                    'type': tool.type,
                                                    'id': tool.id,
                                                    'content': tool.content
                                                },
                                                'passed': False,
                                                'test': True,
                                                'create_at': lesson.create_at,
                                                'lesson_permissions': {
                                                    'bu': {
                                                        'name': bu2.name,
                                                        'id': bu2.id
                                                    },
                                                    "need_manager": 0,
                                                    'id': les_permission.id
                                                },
                                            }
                                            list_.append(data)
                                        else:
                                            data = {
                                                "img_src": lesson.img_src,
                                                'tags': [],
                                                "lecturer": 'null',
                                                # 'oprt': {
                                                #     'id': oper.id,
                                                #     'name': oper.name,
                                                #     'cls': {
                                                #         'id': lescls.id,
                                                #         'name': lescls.name
                                                #     }
                                                # },
                                                'contents': lesson.content,
                                                'id': lesson.id,
                                                'name': lesson.name,
                                                'type': lesson.type,
                                                'tools': {
                                                    'name': tool.name,
                                                    'type': tool.type,
                                                    'id': tool.id,
                                                    'content': tool.content
                                                },
                                                'passed': False,
                                                'test': False,
                                                'create_at': lesson.create_at,
                                                'lesson_permissions': {
                                                    'bu': {
                                                        'name': bu2.name,
                                                        'id': bu2.id
                                                    },
                                                    "need_manager": 0,
                                                    'id': les_permission.id
                                                },
                                            }
                                            list_.append(data)
                                else:
                                    if ques:
                                        data = {
                                            "img_src": lesson.img_src,
                                            'tags': [],
                                            "lecturer": 'null',
                                            # 'oprt': {
                                            #     'id': oper.id,
                                            #     'name': oper.name,
                                            #     'cls': {
                                            #         'id': lescls.id,
                                            #         'name': lescls.name
                                            #     }
                                            # },
                                            'contents': lesson.content,
                                            'id': lesson.id,
                                            'name': lesson.name,
                                            'type': lesson.type,
                                            'tools': [],
                                            'passed': False,
                                            'test': True,
                                            'create_at': lesson.create_at,
                                            'lesson_permissions': {
                                                'bu': {
                                                    'name': bu2.name,
                                                    'id': bu2.id
                                                },
                                                "need_manager": 0,
                                                'id': les_permission.id
                                            },
                                        }
                                        list_.append(data)
                                    else:
                                        data = {
                                            "img_src": lesson.img_src,
                                            'tags': [],
                                            "lecturer": 'null',
                                            # 'oprt': {
                                            #     'id': oper.id,
                                            #     'name': oper.name,
                                            #     'cls': {
                                            #         'id': lescls.id,
                                            #         'name': lescls.name
                                            #     }
                                            # },
                                            'contents': lesson.content,
                                            'id': lesson.id,
                                            'name': lesson.name,
                                            'type': lesson.type,
                                            'tools': [],
                                            'passed': False,
                                            'test': False,
                                            'create_at': lesson.create_at,
                                            'lesson_permissions': {
                                                'bu': {
                                                    'name': bu2.name,
                                                    'id': bu2.id
                                                },
                                                "need_manager": 0,
                                                'id': les_permission.id
                                            },
                                        }
                                        list_.append(data)
                list2 = []
                for i in range(len(list_)):
                    if list_[i] != {}:
                        re_list = []
                        re_list.append(list_[i].get('tools'))
                        for j in range(i + 1, len(list_)):
                            if list_[i].get('id') == list_[j].get('id'):
                                re_list.append(list_[j].get('tools'))
                                list_[i]['tools'] = re_list
                                list_[j] = {}
                        if type(list_[i]['tools']) == list:
                            pass
                        else:
                            list_[i]['tools'] = [list_[i]['tools']]
                        list2.append(list_[i])
                return jsonify(list2)
            elif user:
                pos = Position.query.filter(Position.id.__eq__(user.pos_id)).first()
                bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos.bu_id)).first()
                if bu:
                    les_permissions = LessonPermission.query.filter(LessonPermission.bu_id.__eq__(bu.id)).all()
                    if les_permissions:
                        for les_permission in les_permissions:
                            bu2 = BusinessUnit.query.filter(BusinessUnit.id.__eq__(les_permission.bu_id)).first()
                            lessons = Lesson.query.filter(Lesson.oper_id.__eq__(subPart_id),
                                                          Lesson.id.__eq__(les_permission.lsn_id)).all()
                            for lesson in lessons:
                                ques = Question.query.filter(Question.lsn_id == lesson.id).first()
                                if lesson.lecturer_id:
                                    oper = Operation.query.filter(Operation.id.__eq__(lesson.oper_id)).first()
                                    lescls = LessonClas.query.filter(LessonClas.id.__eq__(oper.cls_id)).first()
                                    staff = User.query.filter(User.id.__eq__(lesson.lecturer_id)).first()
                                    pos1 = Position.query.filter(Position.id.__eq__(staff.pos_id)).first()
                                    bu1 = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos1.bu_id)).first()
                                    tools = Tool.query.filter(Tool.lsn_id.__eq__(lesson.id)).all()
                                    if tools:
                                        for tool in tools:
                                            if ques:
                                                data = {
                                                    "img_src": lesson.img_src,
                                                    'tags': [],
                                                    "lecturer": {
                                                        'name': staff.name,
                                                        'avatar': staff.img_src,
                                                        'lessons': [],
                                                        'pos': {
                                                            'id': pos1.id,
                                                            'name': pos1.name,
                                                            'bu': {
                                                                'name': bu1.name,
                                                                'id': bu1.id
                                                            },
                                                        }
                                                    },
                                                    'oprt': {
                                                        'id': oper.id,
                                                        'name': oper.name,
                                                        'cls': {
                                                            'id': lescls.id,
                                                            'name': lescls.name
                                                        }
                                                    },
                                                    'contents': lesson.content,
                                                    'id': lesson.id,
                                                    'name': lesson.name,
                                                    'type': lesson.type,
                                                    'tools': {
                                                        'name': tool.name,
                                                        'type': tool.type,
                                                        'id': tool.id,
                                                        'content': tool.content
                                                    },
                                                    'passed': False,
                                                    'test': True,
                                                    'create_at': lesson.create_at,
                                                    'lesson_permissions': {
                                                        'bu': {
                                                            'name': bu2.name,
                                                            'id': bu2.id
                                                        },
                                                        "need_manager": 0,
                                                        'id': les_permission.id
                                                    },
                                                }
                                                list_.append(data)
                                            else:
                                                data = {
                                                    "img_src": lesson.img_src,
                                                    'tags': [],
                                                    "lecturer": {
                                                        'name': staff.name,
                                                        'avatar': staff.img_src,
                                                        'lessons': [],
                                                        'pos': {
                                                            'id': pos1.id,
                                                            'name': pos1.name,
                                                            'bu': {
                                                                'name': bu1.name,
                                                                'id': bu1.id
                                                            },
                                                        }
                                                    },
                                                    'oprt': {
                                                        'id': oper.id,
                                                        'name': oper.name,
                                                        'cls': {
                                                            'id': lescls.id,
                                                            'name': lescls.name
                                                        }
                                                    },
                                                    'contents': lesson.content,
                                                    'id': lesson.id,
                                                    'name': lesson.name,
                                                    'type': lesson.type,
                                                    'tools': {
                                                        'name': tool.name,
                                                        'type': tool.type,
                                                        'id': tool.id,
                                                        'content': tool.content
                                                    },
                                                    'passed': False,
                                                    'test': False,
                                                    'create_at': lesson.create_at,
                                                    'lesson_permissions': {
                                                        'bu': {
                                                            'name': bu2.name,
                                                            'id': bu2.id
                                                        },
                                                        "need_manager": 0,
                                                        'id': les_permission.id
                                                    },
                                                }
                                                list_.append(data)
                                    else:
                                        if ques:
                                            data = {
                                                "img_src": lesson.img_src,
                                                'tags': [],
                                                "lecturer": {
                                                    'name': staff.name,
                                                    'avatar': staff.img_src,
                                                    'lessons': [],
                                                    'pos': {
                                                        'id': pos1.id,
                                                        'name': pos1.name,
                                                        'bu': {
                                                            'name': bu1.name,
                                                            'id': bu1.id
                                                        },
                                                    }
                                                },
                                                'oprt': {
                                                    'id': oper.id,
                                                    'name': oper.name,
                                                    'cls': {
                                                        'id': lescls.id,
                                                        'name': lescls.name
                                                    }
                                                },
                                                'contents': lesson.content,
                                                'id': lesson.id,
                                                'name': lesson.name,
                                                'type': lesson.type,
                                                'tools': [],
                                                'passed': False,
                                                'test': True,
                                                'create_at': lesson.create_at,
                                                'lesson_permissions': {
                                                    'bu': {
                                                        'name': bu2.name,
                                                        'id': bu2.id
                                                    },
                                                    "need_manager": 0,
                                                    'id': les_permission.id
                                                },
                                            }
                                            list_.append(data)
                                        else:
                                            data = {
                                                "img_src": lesson.img_src,
                                                'tags': [],
                                                "lecturer": {
                                                    'name': staff.name,
                                                    'avatar': staff.img_src,
                                                    'lessons': [],
                                                    'pos': {
                                                        'id': pos1.id,
                                                        'name': pos1.name,
                                                        'bu': {
                                                            'name': bu1.name,
                                                            'id': bu1.id
                                                        },
                                                    }
                                                },
                                                'oprt': {
                                                    'id': oper.id,
                                                    'name': oper.name,
                                                    'cls': {
                                                        'id': lescls.id,
                                                        'name': lescls.name
                                                    }
                                                },
                                                'contents': lesson.content,
                                                'id': lesson.id,
                                                'name': lesson.name,
                                                'type': lesson.type,
                                                'tools': [],
                                                'passed': False,
                                                'test': False,
                                                'create_at': lesson.create_at,
                                                'lesson_permissions': {
                                                    'bu': {
                                                        'name': bu2.name,
                                                        'id': bu2.id
                                                    },
                                                    "need_manager": 0,
                                                    'id': les_permission.id
                                                },
                                            }
                                            list_.append(data)
                                else:
                                    tools = Tool.query.filter(Tool.lsn_id.__eq__(lesson.id)).all()
                                    if tools:
                                        for tool in tools:
                                            if ques:
                                                data = {
                                                    "img_src": lesson.img_src,
                                                    'tags': [],
                                                    "lecturer": 'null',
                                                    # 'oprt': {
                                                    #     'id': oper.id,
                                                    #     'name': oper.name,
                                                    #     'cls': {
                                                    #         'id': lescls.id,
                                                    #         'name': lescls.name
                                                    #     }
                                                    # },
                                                    'contents': lesson.content,
                                                    'id': lesson.id,
                                                    'name': lesson.name,
                                                    'type': lesson.type,
                                                    'tools': {
                                                        'name': tool.name,
                                                        'type': tool.type,
                                                        'id': tool.id,
                                                        'content': tool.content
                                                    },
                                                    'passed': False,
                                                    'test': True,
                                                    'create_at': lesson.create_at,
                                                    'lesson_permissions': {
                                                        'bu': {
                                                            'name': bu2.name,
                                                            'id': bu2.id
                                                        },
                                                        "need_manager": 0,
                                                        'id': les_permission.id
                                                    },
                                                }
                                                list_.append(data)
                                            else:
                                                data = {
                                                    "img_src": lesson.img_src,
                                                    'tags': [],
                                                    "lecturer": 'null',
                                                    # 'oprt': {
                                                    #     'id': oper.id,
                                                    #     'name': oper.name,
                                                    #     'cls': {
                                                    #         'id': lescls.id,
                                                    #         'name': lescls.name
                                                    #     }
                                                    # },
                                                    'contents': lesson.content,
                                                    'id': lesson.id,
                                                    'name': lesson.name,
                                                    'type': lesson.type,
                                                    'tools': {
                                                        'name': tool.name,
                                                        'type': tool.type,
                                                        'id': tool.id,
                                                        'content': tool.content
                                                    },
                                                    'passed': False,
                                                    'test': False,
                                                    'create_at': lesson.create_at,
                                                    'lesson_permissions': {
                                                        'bu': {
                                                            'name': bu2.name,
                                                            'id': bu2.id
                                                        },
                                                        "need_manager": 0,
                                                        'id': les_permission.id
                                                    },
                                                }
                                                list_.append(data)
                                    else:
                                        if ques:
                                            data = {
                                                "img_src": lesson.img_src,
                                                'tags': [],
                                                "lecturer": 'null',
                                                # 'oprt': {
                                                #     'id': oper.id,
                                                #     'name': oper.name,
                                                #     'cls': {
                                                #         'id': lescls.id,
                                                #         'name': lescls.name
                                                #     }
                                                # },
                                                'contents': lesson.content,
                                                'id': lesson.id,
                                                'name': lesson.name,
                                                'type': lesson.type,
                                                'tools': [],
                                                'passed': False,
                                                'test': True,
                                                'create_at': lesson.create_at,
                                                'lesson_permissions': {
                                                    'bu': {
                                                        'name': bu2.name,
                                                        'id': bu2.id
                                                    },
                                                    "need_manager": 0,
                                                    'id': les_permission.id
                                                },
                                            }
                                            list_.append(data)
                                        else:
                                            data = {
                                                "img_src": lesson.img_src,
                                                'tags': [],
                                                "lecturer": 'null',
                                                # 'oprt': {
                                                #     'id': oper.id,
                                                #     'name': oper.name,
                                                #     'cls': {
                                                #         'id': lescls.id,
                                                #         'name': lescls.name
                                                #     }
                                                # },
                                                'contents': lesson.content,
                                                'id': lesson.id,
                                                'name': lesson.name,
                                                'type': lesson.type,
                                                'tools': [],
                                                'passed': False,
                                                'test': False,
                                                'create_at': lesson.create_at,
                                                'lesson_permissions': {
                                                    'bu': {
                                                        'name': bu2.name,
                                                        'id': bu2.id
                                                    },
                                                    "need_manager": 0,
                                                    'id': les_permission.id
                                                },
                                            }
                                            list_.append(data)
                    list2 = []
                    for i in range(len(list_)):
                        if list_[i] != {}:
                            re_list = []
                            re_list.append(list_[i].get('tools'))
                            for j in range(i + 1, len(list_)):
                                if list_[i].get('id') == list_[j].get('id'):
                                    re_list.append(list_[j].get('tools'))
                                    list_[i]['tools'] = re_list
                                    list_[j] = {}
                            if type(list_[i]['tools']) == list:
                                pass
                            else:
                                list_[i]['tools'] = [list_[i]['tools']]
                            list2.append(list_[i])
                    return jsonify(list2)
                else:
                    return jsonify([])
        else:
            return jsonify([])

class LessonResource3(Resource):
    def get(self,user_id):
        list1 = []
        be_thumbs = []
        be_collected = []
        user = User.query.filter(User.id.__eq__(user_id)).first()
        pos = Position.query.filter(Position.id.__eq__(user.pos_id)).first()
        bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos.bu_id)).first()
        if bu:
            les_permissions = LessonPermission.query.filter(LessonPermission.bu_id.__eq__(bu.id)).all()
            for les_permission in les_permissions:
                bu1 = BusinessUnit.query.filter(BusinessUnit.id.__eq__(les_permission.bu_id)).first()
                lessons = Lesson.query.filter(Lesson.id.__eq__(les_permission.lsn_id),Lesson.recommended.__eq__(1)).all()
                for lesson in lessons:
                    ques = Question.query.filter(Question.lsn_id == lesson.id).first()
                    if lesson.lecturer_id:
                        oper = Operation.query.filter(Operation.id.__eq__(lesson.oper_id)).first()
                        lescls = LessonClas.query.filter(LessonClas.id.__eq__(oper.cls_id)).first()
                        staff = User.query.filter(User.id.__eq__(lesson.lecturer_id)).first()
                        thumbs = LessonThumb.query.filter(LessonThumb.staff_id.__eq__(user_id)).all()
                        for thumb in thumbs:
                            be_thumbs.append(thumb.staff_id)
                        lsn_collects = LessonCollection.query.filter(LessonCollection.staff_id.__eq__(user_id)).all()
                        for lsn_collect in lsn_collects:
                            be_collected.append(lsn_collect.staff_id)
                        if ques:
                            data = {
                                "be_thumbs": be_thumbs,
                                "img_src": lesson.img_src,
                                'tags': [],
                                "lecturer": {
                                    'name': staff.name,
                                    'avatar': staff.img_src,
                                    'lessons': [],
                                    'pos': {
                                        'id': pos.id,
                                        'name': pos.name,
                                        'bu': {
                                            'name': bu.name,
                                            'id': bu.id
                                        },
                                    }
                                },
                                'oprt': {
                                    'id': oper.id,
                                    'name': oper.name,
                                    'cls': {
                                        'id': lescls.id,
                                        'name': lescls.name
                                    }
                                },
                                'contents': lesson.content,
                                'id': lesson.id,
                                'name': lesson.name,
                                'be_collected': be_collected,
                                'type': lesson.type,
                                'passed': False,
                                'test': True,
                                'create_at': lesson.create_at,
                                'lesson_permissions': {
                                    'bu': {
                                        'name': bu1.name,
                                        'id': bu1.id
                                    },
                                    "need_manager": 0,
                                    'id': les_permission.id
                                },
                            }
                            list1.append(data)
                        else:
                            data = {
                                "be_thumbs": be_thumbs,
                                "img_src": lesson.img_src,
                                'tags': [],
                                "lecturer": {
                                    'name': staff.name,
                                    'avatar': staff.img_src,
                                    'lessons': [],
                                    'pos': {
                                        'id': pos.id,
                                        'name': pos.name,
                                        'bu': {
                                            'name': bu.name,
                                            'id': bu.id
                                        },
                                    }
                                },
                                'oprt': {
                                    'id': oper.id,
                                    'name': oper.name,
                                    'cls': {
                                        'id': lescls.id,
                                        'name': lescls.name
                                    }
                                },
                                'contents': lesson.content,
                                'id': lesson.id,
                                'name': lesson.name,
                                'be_collected': be_collected,
                                'type': lesson.type,
                                'passed': False,
                                'test': False,
                                'create_at': lesson.create_at,
                                'lesson_permissions': {
                                    'bu': {
                                        'name': bu1.name,
                                        'id': bu1.id
                                    },
                                    "need_manager": 0,
                                    'id': les_permission.id
                                },
                            }
                            list1.append(data)
                    else:
                        oper = Operation.query.filter(Operation.id.__eq__(lesson.oper_id)).first()
                        lescls = LessonClas.query.filter(LessonClas.id.__eq__(oper.cls_id)).first()
                        thumbs = LessonThumb.query.filter(LessonThumb.staff_id.__eq__(user_id)).all()
                        for thumb in thumbs:
                            be_thumbs.append(thumb.staff_id)
                        lsn_collects = LessonCollection.query.filter(LessonCollection.staff_id.__eq__(user_id)).all()
                        for lsn_collect in lsn_collects:
                            be_collected.append(lsn_collect.staff_id)
                        if ques:
                            data = {
                                "be_thumbs": be_thumbs,
                                "img_src": lesson.img_src,
                                'tags': [],
                                "lecturer": {},
                                'oprt': {
                                    'id': oper.id,
                                    'name': oper.name,
                                    'cls': {
                                        'id': lescls.id,
                                        'name': lescls.name
                                    }
                                },
                                'contents': lesson.content,
                                'id': lesson.id,
                                'name': lesson.name,
                                'be_collected': be_collected,
                                'type': lesson.type,
                                'passed': False,
                                'test': True,
                                'create_at': lesson.create_at,
                                'lesson_permissions': {
                                    'bu': {
                                        'name': bu1.name,
                                        'id': bu1.id
                                    },
                                    "need_manager": 0,
                                    'id': les_permission.id
                                },
                            }
                            list1.append(data)
                        else:
                            data = {
                                "be_thumbs": be_thumbs,
                                "img_src": lesson.img_src,
                                'tags': [],
                                "lecturer": {},
                                'oprt': {
                                    'id': oper.id,
                                    'name': oper.name,
                                    'cls': {
                                        'id': lescls.id,
                                        'name': lescls.name
                                    }
                                },
                                'contents': lesson.content,
                                'id': lesson.id,
                                'name': lesson.name,
                                'be_collected': be_collected,
                                'type': lesson.type,
                                'passed': False,
                                'test': False,
                                'create_at': lesson.create_at,
                                'lesson_permissions': {
                                    'bu': {
                                        'name': bu1.name,
                                        'id': bu1.id
                                    },
                                    "need_manager": 0,
                                    'id': les_permission.id
                                },
                            }
                            list1.append(data)
            return jsonify(list1)
        else:
            return jsonify([])

class LessonResource4(Resource):
    def post(self,lsn_id):
        parser = reqparse.RequestParser()
        parser.add_argument(name='is_look', type=int)
        parse = parser.parse_args()
        is_look = parse.get('is_look')
        lsn = Lesson.query.filter(Lesson.id.__eq__(lsn_id)).first()
        if lsn:
            lsn.is_look = is_look
            db.session.commit()
            return jsonify({'msg': '设置成功！'})
        else:
            return jsonify({'err': '暂无信息！'})
