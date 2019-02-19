from flask import jsonify
from flask_restful import Resource

from App.models import Teacher


class TeacherResource(Resource):
    def get(self):
        teachers = Teacher.query.all()
        list_ = []
        for teacher in teachers:
            data = {
                'name': teacher.name
            }
            list_.append(data)
        return jsonify(list_)