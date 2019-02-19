from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import News,  db

class StaffBannerResource(Resource):
    def get(self):
        news = News.query.filter(News.is_banner.__eq__(1)).all()
        list_ = []
        if news:
            for new in news:
                data = {
                    'content':new.content,
                    'img_src':new.img_src,
                    'name':new.name,
                    'brief':new.brief,
                    'id':new.id,
                    'create_at':new.create_at
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='news', type=str)
        parse = parser.parse_args()
        news = parse.get('news')
        news = eval(news)
        newess = News.query.all()
        for newes in newess:
            newes.is_banner = 0
            db.session.add(newes)
            db.session.commit()
        for n_id in news['news_ids']:
            new = News.query.filter(News.id.__eq__(n_id)).first()
            new.is_banner = 1
            db.session.add(new)
            db.session.commit()

        return jsonify({'msg': '设置成功！'})





        # news =  News.query.all()
        # newcls1 = NewsClas.query.filter(NewsClas.id.__eq__(news[-1].cls_id)).first()
        # newcls2 = NewsClas.query.filter(NewsClas.id.__eq__(news[-2].cls_id)).first()
        # newcls3 = NewsClas.query.filter(NewsClas.id.__eq__(news[-3].cls_id)).first()
        # data = {
        #     'content':news[-1].content,
        #     'img_src':news[-1].img_src,
        #     'cls':{
        #         'name':newcls1.name,
        #         'id':newcls1.id
        #     },
        #     'name':news[-1].name,
        #     'brief':news[-1].brief,
        #     'id':news[-1].id,
        #     'create_at':news[-1].create_at
        # },{
        #     'content':news[-2].content,
        #     'img_src':news[-2].img_src,
        #     'cls':{
        #         'name':newcls2.name,
        #         'id':newcls2.id
        #     },
        #     'name':news[-2].name,
        #     'brief':news[-2].brief,
        #     'id':news[-2].id,
        #     'create_at':news[-2].create_at
        # },{
        #     'content':news[-3].content,
        #     'img_src':news[-3].img_src,
        #     'cls':{
        #         'name':newcls3.name,
        #         'id':newcls3.id
        #     },
        #     'name':news[-3].name,
        #     'brief':news[-3].brief,
        #     'id':news[-3].id,
        #     'create_at':news[-3].create_at
        # }
        # return jsonify(data)