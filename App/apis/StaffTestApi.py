import datetime

from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import Question, Testing, db, User
from sqlalchemy import extract, and_


class StaffTestResource(Resource):
    def get(self,lsn_id):
        quess  = Question.query.filter(Question.lsn_id.__eq__(lsn_id)).all()
        list_ = []
        if quess:
            for ques in quess:
                data = {
                    'id':ques.id,
                    'content':ques.content,
                    'correct_option':ques.correct_option,
                    'other_option':ques.other_option
                }
                list_.append(data)
            return jsonify(list_)

class StaffTestResource1(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='lsn_id', type=int)
        parser.add_argument(name='staff_id', type=int)
        parser.add_argument(name='score', type=float)
        parse = parser.parse_args()
        lsn_id = parse.get('lsn_id')
        staff_id = parse.get('staff_id')
        score = parse.get('score')

        year_ = datetime.datetime.now().year
        month_ = datetime.datetime.now().month
        day_ = datetime.datetime.now().day
        user_ = User.query.filter(User.id == staff_id, and_(
            extract('year', User.update_time) == year_,
            extract('month', User.update_time) == month_,
            extract('day', User.update_time) == day_
        )).first()
        user = User.query.filter(User.id==staff_id).first()
        if user:
            if score == 1.0:
                if user.passed:
                    str1 = user.passed + '#' + str(lsn_id)
                    str2 = str1.split('#')
                    str3 = list(set(str2))
                    user.passed = "#".join(str3)
                    user.fullmarks = "#".join(str3)
                    test = Testing()
                    test.lsn_id = lsn_id
                    test.staff_id = staff_id
                    test.score = score
                    db.session.add(test)
                    db.session.commit()

                    if user_:
                        pass
                    else:
                        u = User.query.filter(User.id == staff_id).first()
                        u.fullmarks = lsn_id
                        db.session.commit()

                    return jsonify({'msg':'提交成功！'})
                else:
                    user.passed = str(lsn_id)
                    user.fullmarks = str(lsn_id)
                    db.session.commit()
                    return jsonify({'msg': '提交成功！'})
            else:
                if user.passed:
                    str1 = user.passed + '#' + str(lsn_id)
                    str2 = str1.split('#')
                    str3 = list(set(str2))
                    user.passed = "#".join(str3)
                    user.passed_dayno = "#".join(str3)
                    test = Testing()
                    test.lsn_id = lsn_id
                    test.staff_id = staff_id
                    test.score = score
                    db.session.add(test)
                    db.session.commit()

                    if user_:
                        pass
                    else:
                        u = User.query.filter(User.id == staff_id).first()
                        u.passed_dayno = lsn_id
                        db.session.commit()

                    return jsonify({'msg':'提交成功！'})
                else:
                    user.passed = str(lsn_id)
                    user.passed_dayno = str(lsn_id)
                    db.session.commit()
                    return jsonify({'msg': '提交成功！'})
        else:
            return jsonify({})