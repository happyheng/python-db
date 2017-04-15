import pymysql


# 1.获取连接对象
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='mytestcon', db='prod', charset='utf8')

# 2.获取游标，来进行查询,这样默认查询的都为tuple列表
# cursor = conn.cursor()
cursor = conn.cursor(pymysql.cursors.DictCursor) # 这样查询的为字典

# 3.执行查询，并获取查询的总行数
# rowNums = cursor.execute('SELECT * FROM student')
# print('查询的行数为' + str(rowNums))


# 4.执行有条件的查询
name = 'happyheng'
selectRowNums = cursor.execute('SELECT * FROM student WHERE name=%s', name)

# 5.遍历结果，获取查询的结果
selectResultList = cursor.fetchall()
for i in range(len(selectResultList)):
    print(selectResultList[i])


# 提交
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()



