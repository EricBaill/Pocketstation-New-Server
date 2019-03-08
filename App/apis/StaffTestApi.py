from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import Question, Testing, db, User


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
        user = User.query.filter(User.id==staff_id).first()
        if user:
            if score == 1.0:
                if user.passed:
                    str1 = user.passed + '#' + str(lsn_id)
                    str2 = str1.split('#')
                    str3 = list(set(str2))
                    user.passed = "#".join(str3)
                    test = Testing()
                    test.lsn_id = lsn_id
                    test.staff_id = staff_id
                    test.score = score
                    db.session.add(test)
                    db.session.commit()
                    return jsonify({'msg':'提交成功！'})
                else:
                    user.passed = str(lsn_id)
                    db.session.commit()
                    return jsonify({'msg': '提交成功！'})
            else:
                test = Testing()
                test.lsn_id = lsn_id
                test.staff_id = staff_id
                test.score = score
                db.session.add(test)
                db.session.commit()
                return jsonify({'msg': '提交成功！'})

        else:
            return jsonify({})