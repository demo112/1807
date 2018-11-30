import pymysql
"""在省表中插入一条记录
    在省表中删除id为8的记录
    在省表中，把id为1的生的名称改为浙江省
    """

db = pymysql.connect(host = 'localhost',
                     user = 'root',
                     database = 'db4',
                     charset = 'utf8',
                     port = 3306
                     )

cursor = db.cursor()
try:
    cursor.execute('insert into sheng values(40, 500000, "海南省");')
    cursor.execute('delete from sheng where id = 8;')
    cursor.execute('update sheng set s_name = "浙江省" where id = 1;')
    db.commit()
    cursor.close()
    db.close()
    print('成功')
except Exception as e:
    db.rollback()
    print("失败", e)
