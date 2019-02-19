from flask import jsonify
from flask_restful import Resource, reqparse
from App.models import LessonClas, Operation, Lesson, Tool, LessonPermission, User, Position, \
    BusinessUnit, UserResource

parser = reqparse.RequestParser()
parser.add_argument(name='name',type=str,required=True,help='名称不能为空')
parser.add_argument(name='content',type=str,required=True,help='内容不能为空')
parser.add_argument(name='type',type=str,required=True,help='类型不能为空')
parser.add_argument(name='hier',type=int)

class UserResourceApi(Resource):
    def get(self,user_id,hier,resId):
        if hier == str(1):
            list_ = []
            lsn_clss = LessonClas.query.all()
            for lsn_cls in lsn_clss:
                data = {
                    'id':lsn_cls.id,
                    'name':lsn_cls.name,
                    'type':'folder',
                    'p_id':2
                }
                list_.append(data)
            return jsonify(list_)
        elif hier == str(2):
            list_1 = []
            opers = Operation.query.filter(Operation.cls_id.__eq__(resId)).all()
            for oper in opers:
                data = {
                    'id': oper.id,
                    'name': oper.name,
                    'type': 'folder',
                    'p_id': 3
                }
                list_1.append(data)
            return jsonify(list_1)
        elif hier == str(3):
            list_2 = []
            user = User.query.filter(User.id.__eq__(user_id)).first()
            pos = Position.query.filter(Position.id.__eq__(user.pos_id)).first()
            bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos.bu_id)).first()
            les_permissions = LessonPermission.query.filter(LessonPermission.bu_id.__eq__(bu.id)).all()
            if les_permissions:
                for les_permission in les_permissions:
                    lesson = Lesson.query.filter(Lesson.oper_id.__eq__(resId),Lesson.id.__eq__(les_permission.lsn_id)).first()
                    if lesson:
                        data = {
                            'id': lesson.id,
                            'name': lesson.name,
                            'type': 'folder',
                            'p_id': 4
                        }
                        list_2.append(data)
                return jsonify(list_2)
            return jsonify([])
        elif hier == str(4):
            list_3 = []
            tools = Tool.query.filter(Tool.lsn_id.__eq__(resId)).all()
            for tool in tools:
                data = {
                    'id': tool.id,
                    'name': tool.name,
                    'type': tool.type,
                    'content': tool.content,
                }
                list_3.append(data)
            return jsonify(list_3)
        else:
            return jsonify([])

class UserResourceApi1(Resource):
    def get(self,resId):
        res = UserResource.query.filter(UserResource.p_id==resId).all()
        list_ = []
        for re in res:
            data = {
                'id':re.id,
                'name':re.name,
                'type':re.type,
                'content':re.content
            }
            list_.append(data)
        return jsonify(list_)

class UserResourceApi2(Resource):
    def get(self):
        list_ = []
        res = UserResource.query.all()
        if res:
            for re in res:
                if re.type == 'folder':
                    pass
                else:
                    data = {
                        'id': re.id,
                        'name': re.name,
                        'type': re.type,
                        'content': re.content
                    }
                    list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])

