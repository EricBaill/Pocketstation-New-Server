#将mysql数据导入到Excel文件

import pymysql
import xlwt

def sql(sql):  # 定义一个执行SQL的函数
    conn = pymysql.connect(host='localhost', user='root', password='123456', db='bbruan', port=3306) # 打开数据库连接
    cursor = conn.cursor()  # 执行数据库的操作是由cursor完成的,使用cursor()方法获取操作游标
    # sql = "select * from job_info"   # 编写sql 查询语句,对应我的表名
    cursor.execute(sql)  # 执行sql语句
    # fields = cursor.description      #获取MYSQL里的数据字段
    # cursor.scroll(0,mode='absolute') #重置游标位置(在同一个程序中执行二次操作用)
    results = cursor.fetchall()  # 获取查询的所有记录
    cursor.close()  # 关闭游标
    conn.close()  # 关闭数据库连接
    return results


def wite_to_excel(name):
    filename = name + '.xls'  # 定义Excel名字
    wbk = xlwt.Workbook()  # 实例化一个Excel
    sheet1 = wbk.add_sheet('经销商用户信息', cell_overwrite_ok=True)  # 添加该Excel的第一个sheet，如有需要可依次添加sheet2等
    fileds = [ '经销商名称', '经销商邮箱']  # 直接定义结果集的各字段名

    results = sql('select name,email from admin')  # 调用函数执行SQL，获取结果集

    for i in range(0, len(fileds)):  # EXCEL新表的第一行  写入字段信息
        sheet1.write(0, i, fileds[i])

    # 执行数据插入
    for row in range(1, len(results) + 1):  # 第0行是字段名，从第一行开始插入数据
        for col in range(0, len(fileds)):  # 依据字段个数进行列的插入
            sheet1.write(row, col, results[row - 1][col])  # 第row行，第col列，插入数据（第1行，第i列，插入results[0][i]）

    # 执行保存
    wbk.save(filename)


wite_to_excel('经销商用户信息')