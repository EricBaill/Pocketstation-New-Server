from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import User, db, Position, BusinessUnit, Order, Lesson, GratitudeStar, LessonCollection, LessonComment, \
    Point, Testing, ToolCollection, TrainingTask, LessonThumb, LessonPermission


class StaffRespource(Resource):
    def get(self):
        users = User.query.all()
        list_ = []
        for user in users:
            poss = Position.query.filter(Position.id.__eq__(user.pos_id)).all()
            for pos in poss:
                bus = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos.bu_id)).all()
                for bu in bus:
                    data = {
                        'id':user.id,
                        'openid':user.openid,
                        'name':user.name,
                        'email':user.email,
                        'avatar':user.img_src,
                        'tel':user.tel,
                        'passwd':user.passwd,
                        'create_at':user.create_at,
                        'pos':{
                            'id':pos.id,
                            'name':pos.name,
                            'is_manager':pos.is_manager,
                            'bu':{
                                'id':bu.id,
                                'name':bu.name
                            }
                        }
                    }
                    list_.append(data)
        return jsonify(list_)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='pos_id', type=int)
        parser.add_argument(name='name', type=str)
        parser.add_argument(name='email', type=str)
        parser.add_argument(name='tel', type=str)
        parser.add_argument(name='passwd', type=str)
        parse = parser.parse_args()
        pos_id = parse.get('pos_id')
        name = parse.get('name')
        email = parse.get('email')
        tel = parse.get('tel')
        passwd = parse.get('passwd')
        user = User()
        user.pos_id = pos_id
        user.name = name
        user.email = email
        user.tel = tel
        user.passwd = passwd
        user.img_src = '/default/avatar_64px.png'
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print(str(e))
        user = User.query.filter(User.email.__eq__(email)).first()
        pos = Position.query.filter(Position.id.__eq__(user.pos_id)).first()
        bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos.bu_id)).first()
        data = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'avatar': user.img_src,
            'tel': user.tel,
            'passwd': user.passwd,
            'create_at': user.create_at,
            'pos': {
                'id': pos.id,
                'name': pos.name,
                'bu': {
                    'id': bu.id,
                    'name': bu.name
                }
            }
        }
        return jsonify(data)

class StaffRespource1(Resource):
    def get(self,user_id):
        user = User.query.filter(User.id.__eq__(user_id)).first()
        if user:
            num = user.dayno
            return jsonify(num)
        else:
            return jsonify({'err':'用户不存在！'})

    def patch(self,user_id):
        parser = reqparse.RequestParser()
        parser.add_argument(name='pos_id', type=int)
        parser.add_argument(name='name', type=str)
        parser.add_argument(name='email', type=str)
        parser.add_argument(name='tel', type=str)
        parser.add_argument(name='avatar', type=str)
        parse = parser.parse_args()
        pos_id = parse.get('pos_id')
        name = parse.get('name')
        email = parse.get('email')
        tel = parse.get('tel')
        avatar = parse.get('avatar')
        user = User.query.filter(User.id.__eq__(user_id)).first()
        if user:
            user.pos_id = pos_id
            user.name = name
            user.email = email
            user.tel = tel
            user.img_src = avatar
            db.session.commit()
            user = User.query.filter(User.email.__eq__(email)).first()
            pos = Position.query.filter(Position.id.__eq__(user.pos_id)).first()
            bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos.bu_id)).first()
            data = {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'avatar': user.img_src,
                'tel': user.tel,
                'passwd': user.passwd,
                'create_at': user.create_at,
                'pos': {
                    'id': pos.id,
                    'name': pos.name,
                    'bu': {
                        'id': bu.id,
                        'name': bu.name
                    }
                }
            }
            return jsonify(data)
        else:
            return jsonify({'err':404})

    def delete(self,user_id):
        user = User.query.filter(User.id.__eq__(user_id)).first()
        if user:
            orders = Order.query.filter(Order.user_id==user.id).all()
            lessons = Lesson.query.filter(Lesson.lecturer_id==user.id).all()
            stars = GratitudeStar.query.filter(GratitudeStar.staff_id==user.id).all()
            collections = LessonCollection.query.filter(LessonCollection.staff_id==user.id).all()
            comments = LessonComment.query.filter(LessonComment.staff_id==user.id).all()
            points = Point.query.filter(Point.staff_id==user.id).all()
            tests = Testing.query.filter(Testing.staff_id==user.id).all()
            toolCollections = ToolCollection.query.filter(ToolCollection.staff_id==user.id).all()
            tasks = TrainingTask.query.filter(TrainingTask.staff_id==user.id).all()
            thumbs = LessonThumb.query.filter(LessonThumb.staff_id==user.id).all()
            if orders:
                for order in orders:
                    db.session.delete(order)
            else:
                pass
            if lessons:
                for les in lessons:
                    permission = LessonPermission.query.filter(LessonPermission.lsn_id==les.id).first()
                    if permission:
                        db.session.delete(permission)
                    else:
                        pass
                    db.session.delete(les)
            else:
                pass
            if stars:
                for star in stars:
                    db.session.delete(star)
            else:
                pass
            if collections:
                for collection in collections:
                    db.session.delete(collection)
            else:
                pass
            if comments:
                for comment in comments:
                    db.session.delete(comment)
            else:
                pass
            if points:
                for point in points:
                    db.session.delete(point)
            else:
                pass
            if tests:
                for test in tests:
                    db.session.delete(test)
            else:
                pass
            if toolCollections:
                for toolCollection in toolCollections:
                    db.session.delete(toolCollection)
            else:
                pass
            if tasks:
                for task in tasks:
                    db.session.delete(task)
            else:
                pass
            if thumbs:
                for thumb in thumbs:
                    db.session.delete(thumb)
            else:
                pass

            db.session.delete(user)
            db.session.commit()
            return jsonify({'msg':'删除成功！'})
        else:
            return jsonify({'err':404})

class StaffRespource2(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='name', type=str)
        parse = parser.parse_args()
        name = parse.get('name')
        users = User.query.filter(User.name.__eq__(name)).all()
        list_ = []
        for user in users:
            pos = Position.query.filter(Position.id.__eq__(user.pos_id)).first()
            bu = BusinessUnit.query.filter(BusinessUnit.id.__eq__(pos.bu_id)).first()
            if user:
                data = {
                    'id': user.id,
                    'name': user.name,
                    'email': user.email,
                    'avatar': user.img_src,
                    'tel': user.tel,
                    'passwd': user.passwd,
                    'create_at': user.create_at,
                    'pos': {
                        'id': pos.id,
                        'name': pos.name,
                        'bu': {
                            'id': bu.id,
                            'name': bu.name
                        }
                    }
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])

