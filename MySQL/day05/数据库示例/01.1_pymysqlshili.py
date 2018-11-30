import pymysql


# 创建数据库连接对象
db = pymysql.connect(host = 'localhost',            # 主机地址
                     user = 'root',                 # 用户名
                     # password = '123456',         # 密码
                     database = 'db4',              # 库
                     charset = 'utf8',              # 编码方式
                     prot = '3306')                 # port  端口号 默认3306


# 2.利用db创建游标对象
cursor = db.cursor()

# 3.利用cursor的execute()方法执行SQL命令
cursor.execute('insert into sheng values(30,400000,"吉林省");')

# 4.提交数据库执行
db.commit()

# 5.关闭游标对象
cursor.close()

# 6.断开数据库连接
db.close()

# 7.rollback()回滚
# db.rollback()


# 格式示范
class Mysql:
    def __init__(self):
        pass

    def fun1(self):
        pass


if __name__ == '__main__':
    db = Mysql()
    db.fun1()
