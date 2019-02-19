from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import Tool, ToolCollection, Lesson, Operation, LessonClas, db


class ToolsResource(Resource):
    def get(self,tool_id):
        staffs = []
        tools = Tool.query.filter(Tool.id.__eq__(tool_id)).first()
        if tools:
            lsn = Lesson.query.filter(Lesson.id.__eq__(tools.lsn_id)).first()
            oper = Operation.query.filter(Operation.id.__eq__(lsn.oper_id)).first()
            lsn_cls = LessonClas.query.filter(LessonClas.id.__eq__(oper.cls_id)).first()
            tool_colls = ToolCollection.query.filter(ToolCollection.tool_id.__eq__(tool_id)).all()
            for tool_coll in tool_colls:
                staffs.append(tool_coll.staff_id)
            data = {
                'id':tools.id,
                'content':tools.content,
                'type':tools.type,
                'name':tools.name,
                'staffs':staffs,
                'lsn':{
                    'name':lsn.name,
                    'id':lsn.id,
                    'oprt':{
                        'name':oper.name,
                        'id':oper.id,
                        'cls':{
                            'name':lsn_cls.name,
                            'id':lsn_cls.id
                        }
                    }
                }
            }
            return jsonify(data)
        else:
            return jsonify({})

    def patch(self,tool_id):
        parser = reqparse.RequestParser()
        parser.add_argument(name='tool_name', type=str)
        parser.add_argument(name='lsn_id', type=int)
        parse = parser.parse_args()
        name = parse.get('tool_name')
        lsn_id = parse.get('lsn_id')
        tool = Tool.query.filter(Tool.id.__eq__(tool_id)).first()
        tool.name = name
        tool.lsn_id = lsn_id
        db.session.commit()
        lsn = Lesson.query.filter(Lesson.id.__eq__(tool.lsn_id)).first()
        oper = Operation.query.filter(Operation.id.__eq__(lsn.oper_id)).first()
        lsn_cls = LessonClas.query.filter(LessonClas.id.__eq__(oper.cls_id)).first()
        data = {
            'id': tool.id,
            'name': tool.name,
            'type': tool.type,
            'content': tool.content,
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
        return jsonify(data)

    def delete(self,tool_id):
        tool = Tool.query.filter(Tool.id.__eq__(tool_id)).first()
        if tool:
            db.session.delete(tool)
            db.session.commit()
            return jsonify({'msg':'删除成功！'})
        else:
            return jsonify({'err':'信息不存在！'})

class ToolsResource1(Resource):
    def get(self):
        tools = Tool.query.all()
        list_ = []
        for tool in tools:
            lsn = Lesson.query.filter(Lesson.id.__eq__(tool.lsn_id)).first()
            oper = Operation.query.filter(Operation.id.__eq__(lsn.oper_id)).first()
            lsn_cls = LessonClas.query.filter(LessonClas.id.__eq__(oper.cls_id)).first()
            data = {
                'id':tool.id,
                'name':tool.name,
                'type':tool.type,
                'content':tool.content,
                'lsn':{
                    'id':lsn.id,
                    'name':lsn.name,
                    'oprt':{
                        'id':oper.id,
                        'name':oper.name,
                        'cls':{
                            'id':lsn_cls.id,
                            'name':lsn_cls.name
                        }
                    }
                }
            }
            list_.append(data)
        return jsonify(list_)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='name', type=str)
        parser.add_argument(name='content', type=str)
        parser.add_argument(name='lsn_id', type=int)
        parser.add_argument(name='type', type=str)
        parse = parser.parse_args()
        name = parse.get('name')
        content = parse.get('content')
        lsn_id = parse.get('lsn_id')
        type = parse.get('type')

        tool = Tool()
        tool.name = name
        tool.content = content
        tool.lsn_id = lsn_id
        tool.type = type
        try:
            db.session.add(tool)
            db.session.commit()
        except Exception as e:
            print(str(e))
        tools = Tool.query.filter(Tool.name.__eq__(name)).first()
        lsn = Lesson.query.filter(Lesson.id.__eq__(tools.lsn_id)).first()
        oper = Operation.query.filter(Operation.id.__eq__(lsn.oper_id)).first()
        lsn_cls = LessonClas.query.filter(LessonClas.id.__eq__(oper.cls_id)).first()
        data = {
            'id': tool.id,
            'name': tool.name,
            'type': tool.type,
            'content': tool.content,
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
        return jsonify(data)

