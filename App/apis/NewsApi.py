from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import db, News, NewsClas

#获取，添加
class NewsResource(Resource):
    def get(self):
        news = News.query.all()
        list_ = []
        for new in news:
            class_id = new.cls_id
            cls_new = NewsClas.query.filter(NewsClas.id.__eq__(class_id)).first()
            data = {
                'id':new.id,
                'name':new.name,
                'content':new.content,
                'brief':new.brief,
                'top':new.top,
                'create_at':new.create_at,
                'img_src':new.img_src,
                'cls':{
                    'name':cls_new.name,
                    'id':cls_new.id
                }
            }
            list_.append(data)
        return jsonify(list_)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='name', type=str)
        parser.add_argument(name='cls_id', type=int)
        parser.add_argument(name='img_src', type=str)
        parser.add_argument(name='brief', type=str)
        parser.add_argument(name='content', type=str)
        parse = parser.parse_args()
        name = parse.get('name')
        cls_id = parse.get('cls_id')
        img_src = parse.get('img_src')
        brief = parse.get('brief')
        content = parse.get('content')
        news = News()
        news.name = name
        news.cls_id = cls_id
        news.img_src = img_src
        news.brief = brief
        news.content = content
        try:
            db.session.add(news)
            db.session.commit()
        except Exception as e:
            print(str(e))
        new = News.query.filter(News.name == name).order_by(News.id.desc()).first()
        id = new.id
        cls_new = NewsClas.query.filter(NewsClas.id.__eq__(cls_id)).first()
        data = {
            'id':id,
            'name':name,
            'img_src':img_src,
            'brief':brief,
            'content':content,
            'cls':{
                'name': cls_new.name,
                'id': cls_new.id
            }
        }
        return jsonify(data)

#修改，删除
class NewsResource1(Resource):
    def get(self,id):
        new = News.query.filter(News.id.__eq__(id)).first()
        if new:
            cls_new = NewsClas.query.filter(NewsClas.id.__eq__(new.cls_id)).first()
            data = {
                'id': new.id,
                'name': new.name,
                'content': new.content,
                'brief': new.brief,
                'top': new.top,
                'create_at': new.create_at,
                'img_src': new.img_src,
                'cls': {
                    'name': cls_new.name,
                    'id': cls_new.id
                }
            }
            return jsonify(data)
        else:
            return jsonify({'err':'信息不存在！'})

    #设置置顶
    def post(self,id):
        parser = reqparse.RequestParser()
        parser.add_argument(name='top', type=int)
        parse = parser.parse_args()
        top = parse.get('top')
        new = News.query.filter(News.id.__eq__(id)).first()
        if new:
            new.top = top
            db.session.commit()
            return jsonify({'msg':'置顶成功！'})
        else:
            return jsonify({'err':'暂无信息！'})

    def put(self,id):
        parser = reqparse.RequestParser()
        parser.add_argument(name='name', type=str)
        parser.add_argument(name='cls_id', type=int)
        parser.add_argument(name='img_src', type=str)
        parser.add_argument(name='brief', type=str)
        parse = parser.parse_args()
        name = parse.get('name')
        cls_id = parse.get('cls_id')
        img_src = parse.get('img_src')
        brief = parse.get('brief')
        new = News.query.filter(News.id.__eq__(id)).first()
        if new:
            new.name = name
            new.img_src = img_src
            new.brief = brief
            new.cls_id = cls_id
            db.session.commit()
            cls_new = NewsClas.query.filter(NewsClas.id.__eq__(cls_id)).first()
            data = {
                'id':id,
                'name':name,
                'img_src':img_src,
                'brief':brief,
                'content':new.content,
                'cls': {
                    'name': cls_new.name,
                    'id': cls_new.id
                }
            }
            return jsonify(data)
        else:
            return jsonify({'err': '暂无信息！'})

    def delete(self,id):
        new = News.query.filter(News.id.__eq__(id)).first()
        if new:
            db.session.delete(new)
            db.session.commit()
            return {'msg': '删除成功！'}
        else:
            return {'msg': '暂无信息！'}

#模糊查询
class NewsResource2(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='name', type=str)
        parse = parser.parse_args()
        name = parse.get('name')
        news = News.query.filter(News.name.like('%'+name+'%')).all()
        if news:
            list_ = []
            for new in news:
                cls_new = NewsClas.query.filter(NewsClas.id.__eq__(new.cls_id)).first()
                data = {
                    'id': new.id,
                    'name': new.name,
                    'img_src': new.img_src,
                    'brief': new.brief,
                    'content': new.content,
                    'cls': {
                        'name': cls_new.name,
                        'id': cls_new.id
                    }
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify({'err': '暂无信息！'})

#按分类查看资讯
class NewsResource3(Resource):
    def get(self,cls_id):
        news = News.query.filter(News.cls_id.__eq__(cls_id)).all()
        new_clas = NewsClas.query.filter(NewsClas.id.__eq__(cls_id)).first()
        if news:
            list_ = []
            for new in news:
                cls_new = NewsClas.query.filter(NewsClas.id.__eq__(new.cls_id)).first()
                data = {
                    'id': new.id,
                    'class_name':new_clas.name,
                    'name': new.name,
                    'img_src': new.img_src,
                    'brief': new.brief,
                    'content': new.content,
                    'cls': {
                        'name': cls_new.name,
                        'id': cls_new.id
                    }
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify({'err': '暂无信息！'})
        