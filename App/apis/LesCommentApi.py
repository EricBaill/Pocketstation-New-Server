from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import LessonComment, Lesson, User, db, Operation, LessonClas


class LesCommentResource(Resource):
    def get(self):
        les_comments = LessonComment.query.all()
        list_ = []
        for les_comment in les_comments:
            user = User.query.filter(User.id.__eq__(les_comment.staff_id)).first()
            lessons = Lesson.query.filter(Lesson.id.__eq__(les_comment.lsn_id)).all()
            for lesson in lessons:
                oper = Operation.query.filter(Operation.id.__eq__(lesson.oper_id)).first()
                cls = LessonClas.query.filter(LessonClas.id.__eq__(oper.cls_id)).first()
                data = {
                    'id':les_comment.id,
                    'content':les_comment.content,
                    'staff':{
                        'id':user.id,
                        'name':user.name,
                        'avatar':user.img_src,
                    },
                    'lsn':{
                        'id':lesson.id,
                        'name':lesson.name,
                        'oprt': {
                            'id': oper.id,
                            'name': oper.name,
                            'cls': {
                                'id': cls.id,
                                'name': cls.name
                            },
                    },
                    }
                }
                list_.append(data)
        return jsonify(list_)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='lsn_id', type=int)
        parser.add_argument(name='staff_id', type=int)
        parser.add_argument(name='content', type=str)
        parse = parser.parse_args()
        lsn_id = parse.get('lsn_id')
        staff_id = parse.get('staff_id')
        content = parse.get('content')

        lsn_comment = LessonComment()
        lsn_comment.lsn_id = lsn_id
        lsn_comment.staff_id = staff_id
        lsn_comment.content = content
        db.session.add(lsn_comment)
        db.session.commit()
        lsn_comments = LessonComment.query.filter(LessonComment.content.__eq__(content)).first()
        user = User.query.filter(User.id.__eq__(lsn_comments.staff_id)).first()
        data = {
            'id': lsn_comments.id,
            'content': content,
            'create_at': lsn_comments.create_at,
            'staff': {
                'name': user.name,
                'avatar': user.img_src
            }
        }
        return jsonify(data)


class LesCommentResource1(Resource):

    def delete(self,id):
        lsn_comment = LessonComment.query.filter(LessonComment.id.__eq__(id)).first()
        if lsn_comment:
            db.session.delete(lsn_comment)
            db.session.commit()
            return jsonify({'msg':'删除成功！'})
        else:
            return jsonify({'err':'暂无信息！'})


class LesCommentResource2(Resource):
    def get(self,lsn_id):
        lsn_comments = LessonComment.query.filter(LessonComment.lsn_id.__eq__(lsn_id)).all()
        list_ = []
        if lsn_comments:
            for lsn_comment in lsn_comments:
                users = User.query.filter(User.id.__eq__(lsn_comment.staff_id)).all()
                for user in users:
                    lessons = Lesson.query.filter(Lesson.id.__eq__(lsn_comment.lsn_id)).all()
                    for lesson in lessons:
                        oper = Operation.query.filter(Operation.id.__eq__(lesson.oper_id)).first()
                        cls = LessonClas.query.filter(LessonClas.id.__eq__(oper.cls_id)).first()
                        data = {
                            'id': lsn_comment.id,
                            'content': lsn_comment.content,
                            'create_at': lsn_comment.create_at,
                            'staff': {
                                'id': user.id,
                                'name': user.name,
                                'avatar': user.img_src,
                            },
                            'lsn': {
                                'id': lesson.id,
                                'name': lesson.name,
                                'oprt': {
                                    'id': oper.id,
                                    'name': oper.name,
                                    'cls': {
                                        'id': cls.id,
                                        'name': cls.name
                                    },
                                },
                            }
                        }
                        list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])

class LesCommentResource3(Resource):
    def get(self,staff_id):
        les_comments = LessonComment.query.filter(LessonComment.staff_id.__eq__(staff_id)).all()
        list_ = []
        if les_comments:
            for les_comment in les_comments:
                user = User.query.filter(User.id.__eq__(les_comment.staff_id)).first()
                lessons = Lesson.query.filter(Lesson.id.__eq__(les_comment.lsn_id)).all()
                for lesson in lessons:
                    oper = Operation.query.filter(Operation.id.__eq__(lesson.oper_id)).first()
                    cls = LessonClas.query.filter(LessonClas.id.__eq__(oper.cls_id)).first()
                    data = {
                        'id': les_comment.id,
                        'content': les_comment.content,
                        'staff': {
                            'id': user.id,
                            'name': user.name,
                            'avatar': user.img_src,
                        },
                        'lsn': {
                            'id': lesson.id,
                            'name': lesson.name,
                            'oprt': {
                                'id': oper.id,
                                'name': oper.name,
                                'cls': {
                                    'id': cls.id,
                                    'name': cls.name
                                },
                            },
                        }
                    }
                    list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])
