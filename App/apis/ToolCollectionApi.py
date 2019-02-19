from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import db, Tool, ToolCollection, User


class ToolCollResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='tool_id', type=int)
        parser.add_argument(name='staff_id', type=int)
        parse = parser.parse_args()
        tool_id = parse.get('tool_id')
        staff_id = parse.get('staff_id')
        tool_coll = ToolCollection()
        tool_coll.tool_id = tool_id
        tool_coll.staff_id = staff_id
        db.session.add(tool_coll)
        db.session.commit()
        tools = Tool.query.filter(Tool.id.__eq__(tool_id)).first()
        data = {
            'id': tools.id,
            'name': tools.name
        }
        return jsonify(data)

class ToolCollResource1(Resource):
    def get(self,user_id):
        tool_colls = ToolCollection.query.filter(ToolCollection.staff_id.__eq__(user_id)).all()
        list_ = []
        for tool_coll in tool_colls:
            users = User.query.filter(User.id.__eq__(tool_coll.staff_id)).all()
            for user in users:
                list_.append(user.id)
        return jsonify(list_)

class ToolCollResource2(Resource):
    def delete(self,user_id,tool_id):
        tool_colls = ToolCollection.query.filter(ToolCollection.staff_id.__eq__(user_id),ToolCollection.tool_id.__eq__(tool_id)).first()
        if tool_colls:
            db.session.delete(tool_colls)
            db.session.commit()
            return jsonify({'msg': '取消收藏成功！'})
        else:
            return jsonify({})

class ToolCollResource3(Resource):
    def get(self,user_id):
        list_ = []
        tool_colls = ToolCollection.query.filter(ToolCollection.staff_id.__eq__(user_id)).all()
        for tool_coll in tool_colls:
            tools = Tool.query.filter(Tool.id.__eq__(tool_coll.tool_id)).all()
            for tool in tools:
                data = {
                    'id':tool.id,
                    'name':tool.name,
                    'content':tool.content,
                    'type':tool.type
                }
                list_.append(data)
        return jsonify(list_)