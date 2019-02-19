from flask_restful import Resource, reqparse
from App.models import A_banner, db
from flask import jsonify


parser = reqparse.RequestParser()
parser.add_argument(name='cover_img',type=str,required=True,help='图片不能为空')
parser.add_argument(name='content',type=str,required=True,help='内容不能为空')

class DealerLbtApi(Resource):
    def get(self):
        new_banner = A_banner.query.all()
        list_ = []
        for ban in new_banner:
            bans = {
                'id':ban.id,
                'cover_img': ban.cover_img,
                'content': ban.content
            }
            list_.append(bans)
        return jsonify(list_)

    def post(self):
        parse = parser.parse_args()
        cover_img = parse.get('cover_img')
        content = parse.get('content')
        new_banner = A_banner()
        new_banner.cover_img = cover_img
        new_banner.content = content
        try:
            db.session.add(new_banner)
            db.session.commit()
        except Exception as e:
            print(str(e))
        banner = A_banner.query.filter(A_banner.cover_img==cover_img)
        if banner.count()>0:
            bann = banner.first()
            data = {
                'id':bann.id,
                'cover_img':cover_img,
                'content':content
            }
            return jsonify(data)

class DealerLbtApi1(Resource):
    def get(self,news_id):
        banner = A_banner.query.filter(A_banner.id==news_id).first()
        if banner:
            data = {
                'id': banner.id,
                'cover_img': banner.cover_img,
                'content': banner.content
            }
            return jsonify(data)
        else:
            return {'msg':"暂无任何信息"}

class DealerLbtApi2(Resource):
    def put(self, news_id):
        parse = parser.parse_args()
        cover_img = parse.get('cover_img')
        content = parse.get('content')
        print(cover_img)
        print(content)
        banner = A_banner.query.filter(A_banner.id==news_id).first()
        banner.cover_img = cover_img
        banner.content = content
        db.session.commit()
        data = {
            'id': banner.id,
            'cover_img': cover_img,
            'content': content
        }
        return jsonify(data)

    def delete(self,news_id):
        banner = A_banner.query.filter(A_banner.id==news_id).first()
        if banner:
            db.session.delete(banner)
            db.session.commit()
            return '删除成功'
        else:
            return {'msg': "暂无任何信息"}
