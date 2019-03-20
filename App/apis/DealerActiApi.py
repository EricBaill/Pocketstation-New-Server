from flask_restful import Resource, reqparse
from App.models import HD, Hd_Ans, Admin, db

from flask import jsonify


class DealerActiApi1(Resource):
    #提交问题
    def post(self,user_id):
        parser = reqparse.RequestParser()
        parser.add_argument(name='type', type=str)
        parser.add_argument(name='ques', type=str)
        parse = parser.parse_args()
        ques = parse.get('ques')
        type = parse.get('type')
        if type == "dealer":
            hd = HD()
            hd.question = ques
            hd.admin_id = user_id
            db.session.add(hd)
            db.session.commit()
            admin = Admin.query.filter(Admin.id.__eq__(user_id)).first()
            hd1s = HD.query.filter(HD.admin_id == user_id).order_by(HD.id.desc()).first()
            data = {
                'id':admin.id,
                'ques_id':hd1s.id,
                'avatar': admin.avatar,
                'name': admin.name,
                'ques': ques,
                'create_at': hd1s.create_at.strftime('%Y/%m/%d'),
                'reply': 0
            }
            return jsonify(data)
        else:
            return jsonify({})


class DealerActiApi2(Resource):
    #提交答案
    def post(self,ques_id,user_id):
        parser = reqparse.RequestParser()
        parser.add_argument(name='reply', type=str)
        parse = parser.parse_args()
        reply = parse.get('reply')
        new_hdans = Hd_Ans()
        new_hdans.ans = reply
        new_hdans.admin_id = user_id
        new_hdans.hd_id = ques_id
        db.session.add(new_hdans)
        db.session.commit()
        admin = Admin.query.filter(Admin.id == user_id).first()
        hd_ans = Hd_Ans.query.filter(Hd_Ans.ans==reply).first()
        data = {
            'id': hd_ans.id,
            'ques_id': ques_id,
            'avatar': admin.avatar,
            'name': admin.name,
            'reply': reply,
            'create_at': hd_ans.create_at.strftime('%Y/%m/%d')
        }
        return jsonify(data)

class DealerActiApi3(Resource):
    #获取某个问题的所有答案
    def get(self,ques_id):
        hd_ans = Hd_Ans.query.filter(Hd_Ans.hd_id.__eq__(ques_id)).all()
        list_ = []
        for hd in hd_ans:
            admins = Admin.query.filter(Admin.id.__eq__(hd.admin_id)).first()
            data = {
                'id': admins.id,
                'avatar': admins.avatar,
                'name': admins.name,
                'reply': hd.ans,
                'reply_id': hd.id,
                'create_at': hd.create_at.strftime('%Y/%m/%d')
            }
            list_.append(data)
        return jsonify(list_)

class DealerActiApi4(Resource):
    #获取所有问题
    def get(self):
        hd = HD.query.all()
        list_ = []
        reply = []
        i = 0
        for h in hd:
            admin = Admin.query.filter(Admin.id == h.admin_id).first()
            hd_ans = Hd_Ans.query.filter(Hd_Ans.hd_id.__eq__(h.id)).all()
            if hd_ans:
                reply.append(len(hd_ans))
                print(reply)
                data = {
                    'id': admin.id,
                    'avatar': admin.avatar,
                    'name': admin.name,
                    'ques_id':h.id,
                    'ques': h.question,
                    'create_at': h.create_at.strftime('%Y/%m/%d'),
                    'reply':reply[i]
                }
                list_.append(data)
                i+=1
            else:
                data = {
                    'id': admin.id,
                    'avatar': admin.avatar,
                    'name': admin.name,
                    'ques_id': h.id,
                    'ques': h.question,
                    'create_at': h.create_at.strftime('%Y/%m/%d'),
                    'reply': 0
                }
                list_.append(data)
        return jsonify(list_)


class DealerActiApi5(Resource):
    def get(self,id):
        hd = HD.query.filter(HD.id.__eq__(id)).first()
        if hd:
            data = {
                'id':hd.id,
                'ques':hd.question,
            }
            return jsonify(data)
        else:
            return jsonify({'err':404})

    def delete(self,id):
        hd = HD.query.filter(HD.id.__eq__(id)).first()
        hd_an = Hd_Ans.query.filter(Hd_Ans.hd_id.__eq__(id)).all()
        if hd and hd_an:
            for h_an in hd_an:
                db.session.delete(h_an)
            db.session.delete(hd)
            db.session.commit()
            return jsonify({'msg':'删除成功！'})
        else:
            return jsonify({'err':'暂无信息！'})







