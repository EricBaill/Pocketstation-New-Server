from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import News, db


class HotMsgResource(Resource):
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
