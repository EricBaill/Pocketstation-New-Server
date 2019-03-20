from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import DealerTraining, db, Experience


class DealerTrainResource(Resource):
    def get(self):
        trains = DealerTraining.query.all()
        list_ = []
        for train in trains:
            data = {
                'id': train.id,
                'title': train.title,
                'cover_img': train.cover_img,
                'lecturer': train.lecturer,
                'content': train.content,
                'desc': train.desc
            }
            list_.append(data)
        return jsonify(list_)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='title', type=str, required=True, help='名称不能为空')
        parser.add_argument(name='cover_img', type=str, required=True, help='图片不能为空')
        parser.add_argument(name='lecturer',type=str,required=True,help='讲师不能为空')
        parser.add_argument(name='content', type=str, required=True, help='内容不能为空')
        parser.add_argument(name='desc', type=str, required=True, help='简介不能为空')
        parse = parser.parse_args()
        title = parse.get('title')
        cover_img = parse.get('cover_img')
        lecturer = parse.get('lecturer')
        content = parse.get('content')
        desc = parse.get('desc')

        train = DealerTraining()
        train.title = title
        train.cover_img = cover_img
        train.lecturer = lecturer
        train.content = content
        train.desc = desc

        try:
            db.session.add(train)
            db.session.commit()
        except Exception as e:
            print(str(e))
        train = DealerTraining.query.filter(DealerTraining.title == title).order_by(DealerTraining.id.desc()).first()
        id = train.id
        data = {
            'id':id,
            'title':title,
            'cover_img':cover_img,
            'lecturer':lecturer,
            'desc':desc
        }
        return jsonify(data)

class DealerTrainResource1(Resource):
    def get(self,id):
        train = DealerTraining.query.filter(DealerTraining.id.__eq__(id)).first()
        if train:
            data = {
                'id': train.id,
                'title': train.title,
                'cover_img': train.cover_img,
                'lecturer': train.lecturer,
                'content': train.content,
                'desc': train.desc
            }
            return jsonify(data)
        else:
            return jsonify({'err':404})

    def put(self,id):
        parser = reqparse.RequestParser()
        parser.add_argument(name='title', type=str, required=True, help='名称不能为空')
        parser.add_argument(name='cover_img', type=str, required=True, help='图片不能为空')
        parser.add_argument(name='content', type=str, required=True, help='内容不能为空')
        parser.add_argument(name='desc', type=str, required=True, help='简介不能为空')
        parse = parser.parse_args()
        title = parse.get('title')
        cover_img = parse.get('cover_img')
        content = parse.get('content')
        desc = parse.get('desc')

        trains = DealerTraining.query.filter(DealerTraining.id.__eq__(id)).all()
        if trains:
            for train in trains:
                train.title = title
                train.cover_img = cover_img
                lecturer = train.lecturer
                train.content = content
                train.desc = desc
                db.session.commit()
                data = {
                    'id': id,
                    'title': title,
                    'lecturer': lecturer,
                    'cover_img': cover_img,
                    'content': content,
                    'desc': desc
                }
                return jsonify(data)
        else:
            return {'code': '404', 'msg': '暂无此信息！'}

    def delete(self, id):
        trains = DealerTraining.query.filter(DealerTraining.id==id).first()
        expers = Experience.query.filter(Experience.dealer_training_id==id).all()
        if expers:
            for exper in expers:
                db.session.delete(exper)
            db.session.commit()
        if trains:
            db.session.delete(trains)
            db.session.commit()

            return {'msg': '删除成功！'}
        else:
            return {'msg': '暂无信息！'}

