import pymysql

db = pymysql.connect(host = 'localhost',
                     user = 'root',
                     database = 'db4',
                     charset = 'utf8',
                     port = 3306
                     )

cursor = db.cursor()
# 执行查询语句
try:
    cursor.execute('select * from sheng;')
    data1 = cursor.fetchone()
    data2 = cursor.fetchmany(3)
    data3 = cursor.fetchall()
    print(data1)
    print('*' * 50)
    print(data2)
    print('*' * 50)
    print(data3)

    db.commit()
    cursor.close()
    db.close()
    print('成功')
except Exception as e:
    db.rollback()
    print("失败", e)
