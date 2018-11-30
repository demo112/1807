import pymysql
"""
    用参数化插入内容
"""

db = pymysql.connect(host = 'localhost',
                     user = 'root',
                     database = 'db4',
                     charset = 'utf8',
                     port = 3306
                     )
cursor = db.cursor()
try:
    name = input('请输入添加的省份')
    id = input('请输入编号')
    cursor.execute('insert into sheng(s_name, s_id) values(%s, %s);', (name, id))
    cursor.execute('delete from sheng where id = 8;')
    cursor.execute('update sheng set s_name = "浙江省" where id = 1;')
    db.commit()
    cursor.close()
    db.close()
    print('成功')
except Exception as e:
    db.rollback()
    print("失败", e)
