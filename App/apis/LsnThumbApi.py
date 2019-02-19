from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import LessonThumb, Lesson, db


class LsnThumbResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='lsn_id', type=int)
        parser.add_argument(name='staff_id', type=int)
        parse = parser.parse_args()
        lsn_id = parse.get('lsn_id')
        staff_id = parse.get('staff_id')

        lsn_thumb = LessonThumb()
        lsn_thumb.lsn_id = lsn_id
        lsn_thumb.staff_id = staff_id
        db.session.add(lsn_thumb)
        db.session.commit()
        lsns = Lesson.query.filter(Lesson.id.__eq__(lsn_id)).first()
        data = {
            'id': lsns.id,
            'name': lsns.name
        }
        return jsonify(data)

class LsnThumbResource1(Resource):
    def get(self,user_id):
        lsn_thumbs = LessonThumb.query.filter(LessonThumb.staff_id.__eq__(user_id)).all()
        list_ = []
        for lsn_thumb in lsn_thumbs:
            lsns = Lesson.query.filter(Lesson.id.__eq__(lsn_thumb.lsn_id)).all()
            for lsn in lsns:
                list_.append(lsn.id)
        return jsonify(list_)

class LsnThumbResource2(Resource):
    def delete(self,user_id,lesson_id):
        lsn_thumbs = LessonThumb.query.filter(LessonThumb.staff_id.__eq__(user_id),LessonThumb.lsn_id.__eq__(lesson_id)).first()
        if lsn_thumbs:
            db.session.delete(lsn_thumbs)
            db.session.commit()
            return jsonify({'msg':'取消点赞成功！'})
        else:
            return jsonify({'err':404})