#读取Excel文件内容批量插入数据库
import random

from pymysql import connect
import xlrd

# 打开xls文件
data = xlrd.open_workbook('经销商名单.xlsx')
# 打开第一张表
table = data.sheets()[1]
# 获取表的行数
nrows = table.nrows
list_ = []
# 循环逐行打印
for i in range(nrows):
    # 取前十三列
    content = table.row_values(i)[1]
    list_.append(content)

seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for j in range(1,len(list_)):
    con = list_[j]
    email = random.choice(seed)+str(j) + random.choice(seed)+'@bbraun.com'
    # passwd = str(j)+str(10)
    #建立连接
    conn = connect(host='localhost', user='root', password='123456', db='bbruan', port=3306)
    # 获取游标
    cur = conn.cursor()
    type = 'dealer'
    bu_id = 10
    create_at = '2018-05-15 02:30:52'
    avatar = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1544011472569&di=0c979013036cc5d17214a99ea8db9d9f&imgtype=0&src=http%3A%2F%2Fpic.90sjimg.com%2Fdesign%2F00%2F67%2F59%2F63%2F58e89bee922a2.png'
    sql = "insert into admin(name,avatar,email,type,create_at,bu_id) values (%s,%s,%s,%s,%s,%s)"
    # 参数化方式传参
    row_count = cur.execute(sql, [con,  avatar, email, type,create_at,bu_id])
    # 显示操作结果
    print("SQL语句影响的行数为%d" % row_count)
    # 统一提交
    conn.commit()
    # 关闭游标　
cur.close()
    # 关闭连接
conn.close()