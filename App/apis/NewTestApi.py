from flask import jsonify, make_response
from flask_restful import Resource, reqparse

from App.models import NewTest, db, User

parser = reqparse.RequestParser()
parser.add_argument(name='staff_id',type=str,required=True,help='员工id不能为空')
parser.add_argument(name='content',type=str,required=True,help='内容不能为空')

class NewTestResource(Resource):
    def post(self):
        headers = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST'
        }

        parse = parser.parse_args()
        staff_id = parse.get('staff_id')
        content = parse.get('content')
        #将字符串转换成字典对象
        content = eval(content)
        #遍历--》将题目与答案对应
        list_1 = []
        list_2 = []
        list_3 = []
        list_4 = []
        d1 = {}
        d2 = {}
        d3 = {}
        d4 = {}
        for key, val in content.items():
            if key == 'sel':
                for v in val:
                    for v1 in v.values():
                        list_1.append(v1)
                    d1[key] = list_1
            elif key == 'blanks':
                for v in val:
                    for v1 in v.values():
                        list_2.append(v1)
                    d2[key] = list_2
            elif key == 'shortAns':
                for v in val:
                    for v1 in v.values():
                        list_3.append(v1)
                    d3[key] = list_3
            elif key == 'picQues':
                for v in val:
                    for v1 in v.values():
                        list_4.append(v1)
                    d4[key] = list_4

        user = User.query.get(staff_id)
        if user:
            newtest = NewTest()
            newtest.staff_id = staff_id
            newtest.staff_name = user.name
            newtest.select = str(d1['sel'])
            newtest.blanks = str(d2['blanks'])
            newtest.shortAns = str(d3['shortAns'])
            newtest.picQues = str(d4['picQues'])

            try:
                db.session.add(newtest)
                db.session.commit()
            except Exception as e:
                print(str(e))
            # return '试题提交成功！'
            return make_response((jsonify({'error_code': 0}), 202, headers))
