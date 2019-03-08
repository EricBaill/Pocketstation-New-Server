import traceback

from flask import jsonify, request
from flask_restful import Resource
from marshmallow import Schema, fields
from openpyxl import load_workbook
from App.models import Question, db, Lesson, Operation, LessonClas
from .schema import QestionSchema


class QuestionSchema(Schema):
    content = fields.String(required=True)
    correct_option = fields.List(fields.String(required=True))
    other_option = fields.List(fields.String(required=True))

class RequestSchema(Schema):
    lsn_id = fields.Int(required=True)
    questions = fields.List(fields.Nested(QuestionSchema))


requst_schema = RequestSchema()

schemas = QestionSchema(many=True)
schema = QestionSchema()



class UserQuesResource(Resource):
    def get(self):
        quess = Question.query.all()
        list_ = []
        for ques in quess:
            lsn = Lesson.query.filter(Lesson.id.__eq__(ques.lsn_id)).first()
            oper = Operation.query.filter(Operation.id.__eq__(lsn.oper_id)).first()
            cls = LessonClas.query.filter(LessonClas.id.__eq__(oper.cls_id)).first()
            data = {
                'id': ques.id,
                'content': ques.content,
                'correct_option': ques.correct_option,
                'other_option': ques.other_option,
                'lsn': {
                    'id': lsn.id,
                    'name': lsn.name,
                    'oprt': {
                        'id': oper.id,
                        'name': oper.name,
                        'cls': {
                            'id': cls.id,
                            'name': cls.name
                        }
                    }
                }
            }
            list_.append(data)
        return jsonify(list_)

    def post(self):
        file = request.files.get('file')
        lsn_id = request.form.get('lsn_id')
        if lsn_id is None or file is None:
            return {"message": "params error!"}, 400

        ques_objs = []
        try:
            wb = load_workbook(file)
            sheet = wb.active
            for row in sheet.rows:
                cols = [col.value for col in row]
                content = None
                other_option = None
                correct_option = None

                tmp = []
                for col in cols:
                    print(col)
                    if col is None:
                        if content is None:
                            content = "#".join(tmp)
                            print("content", content)
                        elif correct_option is None:
                            correct_option = "#".join(tmp)
                            print("correct_option", correct_option)
                        tmp = []
                    else:
                        tmp.append(str(col))
                other_option = "#".join(tmp)
                print("other_option", other_option)

                obj = Question(lsn_id=lsn_id, content=content, correct_option=correct_option,other_option=other_option)
                ques_objs.append(obj)

            db.session.add_all(ques_objs)
            db.session.commit()
            return schemas.dump(ques_objs)
        except Exception as e:
            db.session.rollback()
            traceback.print_exc()
            return {"message": "文件格式错误"}, 406


class UserQuesResource1(Resource):
    def delete(self,ques_id):
        ques = Question.query.filter(Question.id.__eq__(ques_id)).first()
        if ques:
            db.session.delete(ques)
            db.session.commit()
            return jsonify({'msg':'删除成功！'})
        else:
            return jsonify({'err':'暂无信息！'})

class UserQuesResource2(Resource):
    def get(self,lsn_id):
        quess = Question.query.filter(Question.lsn_id.__eq__(lsn_id)).all()
        list_ = []
        if quess:
            for ques in quess:
                lsn = Lesson.query.filter(Lesson.id.__eq__(ques.lsn_id)).first()
                oper = Operation.query.filter(Operation.id.__eq__(lsn.oper_id)).first()
                cls = LessonClas.query.filter(LessonClas.id.__eq__(oper.cls_id)).first()
                data = {
                    'id': ques.id,
                    'content': ques.content,
                    'correct_option': ques.correct_option,
                    'other_option': ques.other_option,
                    'lsn': {
                        'id': lsn.id,
                        'name': lsn.name,
                        'oprt': {
                            'id': oper.id,
                            'name': oper.name,
                            'cls': {
                                'id': cls.id,
                                'name': cls.name
                            }
                        }
                    }
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])
