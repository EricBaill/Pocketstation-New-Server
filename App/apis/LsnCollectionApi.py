from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import LessonCollection, db, Lesson, User


class LsnCollectionResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='lsn_id', type=int)
        parser.add_argument(name='staff_id', type=int)
        parse = parser.parse_args()
        lsn_id = parse.get('lsn_id')
        staff_id = parse.get('staff_id')
        lsn_coll = LessonCollection()
        lsn_coll.lesson_id = lsn_id
        lsn_coll.staff_id = staff_id
        db.session.add(lsn_coll)
        db.session.commit()
        lsns = Lesson.query.filter(Lesson.id.__eq__(lsn_id)).first()
        data = {
            'id':lsns.id,
            'name':lsns.name
        }
        return jsonify(data)

class LsnCollectionResource1(Resource):
    def get(self,user_id):
        lsn_colls = LessonCollection.query.filter(LessonCollection.staff_id.__eq__(user_id)).all()
        list_ = []
        for lsn_coll in lsn_colls:
            users = User.query.filter(User.id.__eq__(lsn_coll.lesson_id)).all()
            for user in users:
                list_.append(user.id)
        return jsonify(list_)

class LsnCollectionResource2(Resource):
    def delete(self,staff_id,lsn_id):
        lsn_colls = LessonCollection.query.filter(LessonCollection.staff_id.__eq__(staff_id),LessonCollection.lesson_id.__eq__(lsn_id)).first()
        if lsn_colls:
            db.session.delete(lsn_colls)
            db.session.commit()
            return jsonify({'msg':'取消收藏成功！'})
        else:
            return jsonify({'err':'暂无信息！'})

class LsnCollectionResource3(Resource):
        def get(self, user_id):
            list_ = []
            les_colls = LessonCollection.query.filter(LessonCollection.staff_id.__eq__(user_id)).all()
            for les_coll in les_colls:
                lessons = Lesson.query.filter(Lesson.id.__eq__(les_coll.lesson_id)).all()
                for lesson in lessons:
                    data = {
                        'id': lesson.id,
                        'name': lesson.name,
                        'content': lesson.content,
                        'type': lesson.type,
                        'img_src': lesson.img_src
                    }
                    list_.append(data)
            return jsonify(list_)