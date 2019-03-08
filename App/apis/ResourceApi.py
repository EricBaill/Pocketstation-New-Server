from flask import jsonify
from flask_restful import Resource, reqparse
from App.models import DealerResource, db

parser = reqparse.RequestParser()
parser.add_argument(name='name',type=str,required=True,help='名称不能为空')
parser.add_argument(name='content',type=str)
parser.add_argument(name='type',type=str,required=True,help='类型不能为空')
parser.add_argument(name='hier',type=int)

class ResourceApi(Resource):
    def get(self,resId):
        res = DealerResource.query.filter(DealerResource.p_id==resId).all()
        list_ = []
        for re in res:
            data = {
                'id':re.id,
                'name':re.name,
                'type':re.type,
                'content':re.content
            }
            list_.append(data)
        return jsonify(list_)


    def delete(self,resId):
        res = DealerResource.query.filter(DealerResource.id.__eq__(resId)).first()
        if res:
            db.session.delete(res)
            db.session.commit()
            return jsonify({'msg':'删除成功！'})
        else:
            return jsonify({})


class ResourceApi1(Resource):
    def get(self):
        res1 = DealerResource.query.filter(DealerResource.type=="folder").all()
        list_ = []
        for re1 in res1:
            data = {
                'id': re1.id,
                'name': re1.name,
                }
            list_.append(data)
        return jsonify(list_)

    def post(self):
        parse = parser.parse_args()
        name = parse.get('name')
        content = parse.get('content')
        type = parse.get('type')
        hier = parse.get('hier')
        re = DealerResource()
        re.name = name
        re.type = type
        re.content = content
        re.p_id = hier
        db.session.add(re)
        db.session.commit()
        if type == 'folder':
            pass
        else:
            res = DealerResource.query.filter(DealerResource.name==name).first()
            id = res.id
            data = {
                'id':id,
                'name':name,
                'content':content,
                'type':type,
                'hier':hier
            }
            return jsonify(data)


class ResourceApi2(Resource):
    def get(self):
        res = DealerResource.query.all()
        list_ = []
        for re in res:
            if re.type != 'folder':
                rs = DealerResource.query.filter(DealerResource.id==re.p_id).all()
                for r in rs:
                    data = {
                        'id':re.id,
                        'name':re.name,
                        'content':re.content,
                        'type':re.type,
                        'hier':{
                            'name':r.name,
                            'id':r.id
                        }
                    }
                    list_.append(data)
        return jsonify(list_)

class ResourceApi3(Resource):
    def put(self,id):
        parse = parser.parse_args()
        name = parse.get('name')
        content = parse.get('content')
        type = parse.get('type')
        hier = parse.get('hier')
        res = DealerResource.query.filter(DealerResource.id.__eq__(id)).first()
        if res:
            res.name = name
            res.content = content
            res.type = type
            res.p_id = hier
            db.session.commit()
            re = DealerResource.query.filter(DealerResource.id.__eq__(hier)).first()
            data = {
                'id': id,
                'name': name,
                'content': content,
                'type': type,
                'hier': {
                    'id':re.p_id,
                    'name':re.name
                }
            }
            return jsonify(data)
        else:
            return jsonify({})

class ResourceApi4(Resource):
    def get(self):
        res = DealerResource.query.all()
        list_ = []
        for re in res:
            if re.type == 'folder':
                rs = DealerResource.query.filter(DealerResource.id == re.p_id).all()
                for r in rs:
                    data = {
                        'id': re.id,
                        'name': re.name,
                        'content': re.content,
                        'type': re.type,
                        'hier': {
                            'name': r.name,
                            'id': r.id
                        }
                    }
                    list_.append(data)
        print(list_)
        return jsonify(list_)

class ResourceApi5(Resource):
    def put(self,resId):
        parser = reqparse.RequestParser()
        parser.add_argument(name='name', type=str, required=True, help='名称不能为空')
        parser.add_argument(name='p_id', type=int)
        parse = parser.parse_args()
        name = parse.get('name')
        p_id = parse.get('p_id')
        res = DealerResource.query.filter(DealerResource.id.__eq__(resId)).first()
        if res:
            res.name = name
            res.p_id = p_id
            db.session.commit()
            return jsonify({'msg':'修改成功！'})
        else:
            return jsonify({'msg':'暂无信息！'})

    def delete(self,resId):
        res = DealerResource.query.filter(DealerResource.id.__eq__(resId)).first()
        if res:
            ress = DealerResource.query.filter(DealerResource.p_id==res.id).all()
            if ress:
                for re in ress:
                    db.session.delete(re)
            db.session.delete(res)
            db.session.commit()
            return jsonify({'msg':'删除成功！'})
        else:
            return jsonify({'msg':'暂无信息！'})

