from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import FAQ, db

parser = reqparse.RequestParser()
parser.add_argument(name='title',type=str,required=True,help='问题不能为空')
parser.add_argument(name='answer',type=str,required=True,help='答案不能为空')

class FaqResource(Resource):
    def get(self):
        faqs = FAQ.query.all()
        list_ = []
        for faq in faqs:
            data = {
                'id':faq.id,
                'title':faq.title,
                'answer':faq.answer
            }
            list_.append(data)
        return jsonify(list_)

    def post(self):
        parse = parser.parse_args()
        title = parse.get('title')
        answer = parse.get('answer')

        faq = FAQ()
        faq.title = title
        faq.answer = answer
        try:
            db.session.add(faq)
            db.session.commit()
        except Exception as e:
            print(str(e))
        fs = FAQ.query.filter(FAQ.title==title).order_by(FAQ.id.desc()).first()
        id = fs.id
        data = {
            'id':id,
            'title':title,
            'answer':answer
        }
        return jsonify(data)

class FaqChanceResource(Resource):
    def get(self,id):
        faq = FAQ.query.filter(FAQ.id.__eq__(id)).first()
        if faq:
            data = {
                'id':faq.id,
                'title':faq.title,
                'answer':faq.answer
            }
            return jsonify(data)
        else:
            return jsonify({"err":404})

    def put(self,id):
        parse = parser.parse_args()
        title = parse.get('title')
        answer = parse.get('answer')

        faqs = FAQ.query.filter(FAQ.id.__eq__(id)).all()
        if faqs:
            for faq in faqs:
                faq.title = title
                faq.answer = answer
                try:
                    db.session.add(faq)
                    db.session.commit()
                except Exception as e:
                    print(str(e))
                data = {
                        'id': id,
                        'title': title,
                        'answer': answer
                }
                return jsonify(data)
        else:
            return {'code':'404','msg ':'暂无此信息！'}

    def delete(self,id):
        faqs = FAQ.query.filter(FAQ.id.__eq__(id)).first()
        if faqs:
            db.session.delete(faqs)
            db.session.commit()

            return {'msg':'删除成功！'}
        else:
            return {'msg':'暂无信息！'}



