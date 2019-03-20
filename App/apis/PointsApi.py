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

        str0 = user.fullmarks
        if user.fullmarks:
            if len(str0.split('#')) <= 8:
                str0 = user.fullmarks.split('#')
                str0 = len(str0) * 2
            else:
                str0 = 16
        else:
            str0 = 0

        str1 = user.passed_dayno
        if user.passed_dayno:
            if len(str1.split('#')) <= 8:
                str1 = user.passed_dayno.split('#')
                str1 = len(str1) * 2
            else:
                str1 = 16
        else:
            str1 = 0

        str2 = user.lesson_dayno
        if user.lesson_dayno:
            if len(str2.split('#')) <= 8:
                str2 = user.lesson_dayno.split('#')
                str2 = len(str2) * 2
            else:
                str2 = 16
        else:
            str2 = 0

        str3 = user.newnumber_day
        if user.newnumber_day:
            if len(str3.split('#')) <= 8:
                str3 = user.newnumber_day.split('#')
                str3 = len(str3) * 2
            else:
                str3 = 16
        else:
            str3 = 0


        str4 = user.toolnumber_day
        if user.toolnumber_day:
            if len(str4.split('#')) <= 8:
                str4 = user.toolnumber_day.split('#')
                str4 = len(str4) * 2
            else:
                str4 = 16
        else:
            str4 = 0

        str5 = user.resnumber_day
        if user.resnumber_day:
            if len(str5.split('#')) <= 8:
                str5 = user.resnumber_day.split('#')
                str5 = len(str5) * 2
            else:
                str5 = 16
        else:
            str5 = 0

        if poin:
            if from_grat or to_grat or user:

                if len(from_grats) <= 8 and len(to_grats) <= 8:
                    l = len(from_grat) * 2
                    l1 = len(to_grat) * 2
                    points = str0 + str1 + str2 + str3 + str4 + str5 + l + l1
                    point = points - poin.sumprice

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

                elif len(from_grats) > 8 and len(to_grats) > 8:
                    l = 8 * 2
                    l1 = 8 * 2
                    points = str0 +  str1 + str2 + str3 + str4 + str5 + l + l1
                    point = points - poin.sumprice

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

                elif len(from_grats) <= 8 and len(to_grats) > 8:
                    l = len(from_grat) * 2
                    l1 = 8 * 2
                    points = str0 +  str1 + str2 + str3 + str4 + str5 + l + l1
                    point = points - poin.sumprice

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

                elif len(from_grats) > 8 and len(to_grats) <= 8:
                    l = 8 * 2
                    l1 = len(to_grat) * 2
                    points = str0 +  str1 + str2 + str3 + str4 + str5 + l + l1
                    point = points - poin.sumprice

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
                if len(from_grats) <= 8 and len(to_grats) <= 8:
                    l = len(from_grat) * 2
                    l1 = len(to_grat) * 2
                    point = str0 + str1 + str2 + str3 + str4 + str5 + l + l1


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

                elif len(from_grats) > 8 and len(to_grats) > 8:
                    l = 8 * 2
                    l1 = 8 * 2
                    point = str0 + str1 + str2 + str3 + str4 + str5 + l + l1

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

                elif len(from_grats) <= 8 and len(to_grats) > 8:
                    l = len(from_grat) * 2
                    l1 = 8 * 2
                    point = str0 + str1 + str2 + str3 + str4 + str5 + l + l1

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

                elif len(from_grats) > 8 and len(to_grats) <= 8:
                    l = 8 * 2
                    l1 = len(to_grat) * 2
                    point = str0 + str1 + str2 + str3 + str4 + str5 + l + l1

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

class Points01(Resource):
    def get(self,staff_id):
        user = User.query.filter(User.id==staff_id).first()
        if user:
            data = {
                'account':user.passed
            }
            return jsonify(data)
        else:
            return jsonify({})

class Points02(Resource):
    def get(self,staff_id):
        user = User.query.filter(User.id==staff_id).first()
        if user:
            data = {
                'account':user.lesson_
            }
            return jsonify(data)
        else:
            return jsonify({})

class Points03(Resource):
    def get(self,staff_id):
        user = User.query.filter(User.id==staff_id).first()
        if user:
            data = {
                'account':user.newnumber
            }
            return jsonify(data)
        else:
            return jsonify({})

class Points04(Resource):
    def get(self,staff_id):
        user = User.query.filter(User.id==staff_id).first()
        if user:
            data = {
                'account':user.toolnumber
            }
            return jsonify(data)
        else:
            return jsonify({})

class Points05(Resource):
    def get(self,staff_id):
        user = User.query.filter(User.id==staff_id).first()
        if user:
            data = {
                'account':user.resnumber
            }
            return jsonify(data)
        else:
            return jsonify({})