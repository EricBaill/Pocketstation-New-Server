list_ = []
data = {
    'id': 1,
    'name':'qq',
    'children':[{
    'id':1,
    'name':'eee',
    },{
    'id':1,
    'name':'eee',
    }]
}
list_.append(data)
list2 = []
for i in range(len(list_)):
    if list_[i] != {}:
        re_list = []
        re_list.append(list_[i].get('children'))
        for j in range(i + 1, len(list_)):
            if list_[i].get('id') == list_[j].get('id'):
                re_list.append(list_[j].get('children'))
                list_[i]['children'] = re_list
                list_[j] = {}
        list2.append(list_[i])
print(list2)