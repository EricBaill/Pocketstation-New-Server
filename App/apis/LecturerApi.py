from flask import jsonify
from flask_restful import Resource

from App.models import  User, Lesson, LessonCollection, LessonThumb


class LecturerResource(Resource):
    def get(self):
        users = User.query.all()
        list_ = []
        list_1 = []
        list_2 = []
        list_3 = []
        result = {}
        result1 = {}
        for user in users:
            lessons = Lesson.query.filter(Lesson.lecturer_id.__eq__(user.id)).all()
            if lessons:
                for lsn in lessons:
                    list_1.append(lsn.lecturer_id)
                    for i in set(list_1):
                        result[i] = list_1.count(i)
        for a,b in result.items():
            user = User.query.filter(User.id.__eq__(a)).first()
            # lsnss = Lesson.query.filter(Lesson.lecturer_id.__eq__(user.id)).all()
            # for lsn in lsnss:
            # thumbs = LessonThumb.query.filter(LessonThumb.lsn_id.__eq__(lsn.id)).all()
            # # lsn_collections = LessonCollection.query.filter(LessonCollection.staff_id.__eq__(user.id)).all()
            # if thumbs:
            #     for thumb in thumbs:
            #         list_2.append(thumb.staff_id)
            #         for j in set(list_2):
            #             result1[j] = list_2.count(j)
            # for c,d in result1.items():
            #     print(c,d)
            data = {
                'name':user.name,
                'avatar':user.img_src,
                'lessons':b,
                # 'be_thumbs':len(list_2),
                # 'be_collected':len(list_3)
            }
            list_.append(data)
        # else:
        #     data = {
        #         'name': user.name,
        #         'avatar': user.img_src,
        #         'lessons': b,
        #         'be_thumbs': 0,
        #         'be_collected':0
        #     }
        return jsonify(list_)


