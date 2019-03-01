from flask import jsonify
from flask_restful import Resource, reqparse

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
                            'finish_at':learn.finish_at,
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
        staff = User.query.filter(User.id==staff_id).first()
        if staff:
            if staff.lesson_:
                str1 = staff.lesson_ + '#' + lsn_id
                str2 = str1.split('#')
                str3 = list(set(str2))
                staff.lesson_ = "#".join(str3)
                db.session.commit()
                return jsonify({'msg':'成功'})
            else:
                staff.lesson_ = lsn_id
                db.session.commit()
                return jsonify({'msg': '成功'})

        else:
            return jsonify({})