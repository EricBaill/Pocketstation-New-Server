from flask import jsonify
from flask_restful import Resource
from App.models import Gratitude, User, Point, db
from sqlalchemy import extract, and_
import datetime


class PointsResource(Resource):
    def get(self,staff_id):
        from_grat = Gratitude.query.filter(Gratitude.from_id.__eq__(staff_id)).all()
        to_grat = Gratitude.query.filter(Gratitude.to_id.__eq__(staff_id)).all()
        user = User.query.filter(User.id.__eq__(staff_id)).first()
        poin = Point.query.filter(Point.staff_id.__eq__(staff_id)).first()

        years = datetime.datetime.now().strftime('%Y')
        months = datetime.datetime.now().strftime('%m')
        days = datetime.datetime.now().strftime('%d')

        from_grats = Gratitude.query.filter(Gratitude.from_id.__eq__(staff_id), and_(
            extract('year', Gratitude.create_at) == years,
            extract('month', Gratitude.create_at) == months,
            extract('day', Gratitude.create_at) == days
        )).all()
        to_grats = Gratitude.query.filter(Gratitude.to_id.__eq__(staff_id), and_(
            extract('year', Gratitude.create_at) == years,
            extract('month', Gratitude.create_at) == months,
            extract('day', Gratitude.create_at) == days
        )).all()

        if poin:
            if from_grat or to_grat or user:

                if len(from_grats) <= 5 and len(to_grats) <= 5:
                    l = len(from_grat)
                    l1 = len(to_grat)
                    num1 = user.dayno + l + l1
                    point = num1 * 2

                    if 0 <= point <= 50:
                        poin.level = '新兵'
                    elif 51 <= point <= 100:
                        poin.level = '列兵'
                    elif 101 <= point <= 200:
                        poin.level = '士官'
                    elif 201 <= point <= 400:
                        poin.level = '尉官'
                    elif 401 <= point <= 700:
                        poin.level = '校官'
                    elif 701 <= point <= 1000:
                        poin.level = '将官'
                    elif point >= 1001:
                        poin.level = '元帅'
                    poin.total_points = point
                    db.session.commit()
                    data = {
                        'points': point,
                        'level': poin.level
                    }
                    return jsonify(data)

                elif len(from_grats) > 5 and len(to_grats) > 5:
                    l = 5
                    l1 = 5
                    num1 = user.dayno + l + l1
                    point = num1 * 2

                    if 0 <= point <= 50:
                        poin.level = '新兵'
                    elif 51 <= point <= 100:
                        poin.level = '列兵'
                    elif 101 <= point <= 200:
                        poin.level = '士官'
                    elif 201 <= point <= 400:
                        poin.level = '尉官'
                    elif 401 <= point <= 700:
                        poin.level = '校官'
                    elif 701 <= point <= 1000:
                        poin.level = '将官'
                    elif point >= 1001:
                        poin.level = '元帅'
                    poin.total_points = point
                    db.session.commit()
                    data = {
                        'points': point,
                        'level': poin.level
                    }
                    return jsonify(data)

                elif len(from_grats) <= 5 and len(to_grats) > 5:
                    l = len(from_grat)
                    l1 = 5
                    num1 = user.dayno + l + l1
                    point = num1 * 2

                    if 0 <= point <= 50:
                        poin.level = '新兵'
                    elif 51 <= point <= 100:
                        poin.level = '列兵'
                    elif 101 <= point <= 200:
                        poin.level = '士官'
                    elif 201 <= point <= 400:
                        poin.level = '尉官'
                    elif 401 <= point <= 700:
                        poin.level = '校官'
                    elif 701 <= point <= 1000:
                        poin.level = '将官'
                    elif point >= 1001:
                        poin.level = '元帅'
                    poin.total_points = point
                    db.session.commit()
                    data = {
                        'points': point,
                        'level': poin.level
                    }
                    return jsonify(data)

                elif len(from_grats) > 5 and len(to_grats) <= 5:
                    l = 5
                    l1 = len(to_grat)
                    num1 = user.dayno + l + l1
                    point = num1 * 2

                    if 0 <= point <= 50:
                        poin.level = '新兵'
                    elif 51 <= point <= 100:
                        poin.level = '列兵'
                    elif 101 <= point <= 200:
                        poin.level = '士官'
                    elif 201 <= point <= 400:
                        poin.level = '尉官'
                    elif 401 <= point <= 700:
                        poin.level = '校官'
                    elif 701 <= point <= 1000:
                        poin.level = '将官'
                    elif point >= 1001:
                        poin.level = '元帅'
                    poin.total_points = point
                    db.session.commit()
                    data = {
                        'points': point,
                        'level': poin.level
                    }
                    return jsonify(data)

        else:

            if from_grat or to_grat or user:
                if len(from_grats) <= 5 and len(to_grats) <= 5:
                    l = len(from_grat)
                    l1 = len(to_grat)
                    num1 = user.dayno + l + l1
                    point = num1 * 2
                    poin = Point()
                    if 0 <= point <= 50:
                        poin.level = '新兵'
                    elif 51 <= point <= 100:
                        poin.level = '列兵'
                    elif 101 <= point <= 200:
                        poin.level = '士官'
                    elif 201 <= point <= 400:
                        poin.level = '尉官'
                    elif 401 <= point <= 700:
                        poin.level = '校官'
                    elif 701 <= point <= 1000:
                        poin.level = '将官'
                    elif point >= 1001:
                        poin.level = '元帅'
                    poin.total_points = point
                    poin.staff_id = staff_id
                    db.session.add(poin)
                    db.session.commit()
                    data = {
                        'points': point,
                        'level': poin.level
                    }
                    return jsonify(data)

                elif len(from_grats) > 5 and len(to_grats) > 5:
                    l = 5
                    l1 = 5
                    num1 = user.dayno + l + l1
                    point = num1 * 2
                    poin = Point()
                    if 0 <= point <= 50:
                        poin.level = '新兵'
                    elif 51 <= point <= 100:
                        poin.level = '列兵'
                    elif 101 <= point <= 200:
                        poin.level = '士官'
                    elif 201 <= point <= 400:
                        poin.level = '尉官'
                    elif 401 <= point <= 700:
                        poin.level = '校官'
                    elif 701 <= point <= 1000:
                        poin.level = '将官'
                    elif point >= 1001:
                        poin.level = '元帅'
                    poin.total_points = point
                    poin.staff_id = staff_id
                    db.session.add(poin)
                    db.session.commit()
                    data = {
                        'points': point,
                        'level': poin.level
                    }
                    return jsonify(data)

                elif len(from_grats) <= 5 and len(to_grats) > 5:
                    l = len(from_grat)
                    l1 = 5
                    num1 = user.dayno + l + l1
                    point = num1 * 2
                    poin = Point()
                    if 0 <= point <= 50:
                        poin.level = '新兵'
                    elif 51 <= point <= 100:
                        poin.level = '列兵'
                    elif 101 <= point <= 200:
                        poin.level = '士官'
                    elif 201 <= point <= 400:
                        poin.level = '尉官'
                    elif 401 <= point <= 700:
                        poin.level = '校官'
                    elif 701 <= point <= 1000:
                        poin.level = '将官'
                    elif point >= 1001:
                        poin.level = '元帅'
                    poin.total_points = point
                    poin.staff_id = staff_id
                    db.session.add(poin)
                    db.session.commit()
                    data = {
                        'points': point,
                        'level': poin.level
                    }
                    return jsonify(data)

                elif len(from_grats) > 5 and len(to_grats) <= 5:
                    l = 5
                    l1 = len(to_grat)
                    num1 = user.dayno + l + l1
                    point = num1 * 2
                    poin = Point()
                    if 0 <= point <= 50:
                        poin.level = '新兵'
                    elif 51 <= point <= 100:
                        poin.level = '列兵'
                    elif 101 <= point <= 200:
                        poin.level = '士官'
                    elif 201 <= point <= 400:
                        poin.level = '尉官'
                    elif 401 <= point <= 700:
                        poin.level = '校官'
                    elif 701 <= point <= 1000:
                        poin.level = '将官'
                    elif point >= 1001:
                        poin.level = '元帅'
                    poin.total_points = point
                    poin.staff_id = staff_id
                    db.session.add(poin)
                    db.session.commit()
                    data = {
                        'points': point,
                        'level': poin.level
                    }
                    return jsonify(data)
