import pymysql


# 1.获取连接对象
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='mytestcon', db='prod', charset='utf8')
cursor = conn.cursor()

# 2.执行插入语句， 批量插入
insertRow = cursor.executemany('INSERT INTO user (name, password, age) VALUES (%s, %s, %s)', [('happyheng', '123456', '22'), ('happyheng2', '123456', '22')])
print('插入的行数为' + str(insertRow))

# 3.得到第一个插入的id
lastInsertId = cursor.lastrowid

# 4.更新
#
#
# 当更新（包括增删改）的格式化数据为一个元组时，使用execute  -----
# 当更新（包括增删改）的格式化数据大于一个元组时，使用executemany ----
updateRow = cursor.execute('UPDATE user SET name = %s WHERE id = %s', ('happyheng123', '1'))
print('更新的行数为' + str(updateRow))


# 5.删除
deleteRow = cursor.execute('DELETE FROM user WHERE id = %s', '1')
print('删除的行数为' + str(deleteRow))


# 提交并close
conn.commit()
cursor.close()
conn.close()


