from pymysql import connect


class MysqlHelp:
    def __init__(self,
                 database,
                 host = 'localhost',
                 user = 'root',
                 # password = '123456',
                 charset = 'utf8',
                 port = 3306):
        self.cur = None
        self.conn = None
        self.database = database
        self.host = host
        self.user = user
        # self.password = password
        self.charset = charset
        self.port = port

    # 打开数据库方法
    def open(self):
        self.conn = connect(host = self.host,
                            user = self.user,
                            database = self.database,
                            # password = self.password,
                            charset = self.charset,
                            port = self.port)
        self.cur = self.conn.cursor()

    # 打关闭数据库方法
    def close(self):
        self.cur.close()
        self.conn.close()

    # 执行SQL语句方法
    def work_on(self, sql, lst=None):
        if lst is None:
            lst = []
        self.open()
        try:
            self.cur.execute(sql, lst)
            self.conn.commit()
            print('OK')
        except Exception as e:
            self.conn.rollback()
            print("错误", e)
        self.close()

    # 查询方法
    def get_all(self, sql, lst=None):
        if lst is None:
            lst = []
        self.open()
        self.cur.execute(sql, lst)
        re = self.cur.fetchall()
        self.close()
        # print('OjbK')

        return re


# # if __name__ == '__main__':
#     # 测试
#     mysql = MysqlHelp('db4')
#     sql_insert = 'insert into sheng(s_name) values("上海市")'
#     mysql.work_on(sql_insert)
#
#     # 测试代码
#     mysql = MysqlHelp('db4')
#     sql_select = 'select * from sheng;'
#     result = mysql.get_all(sql_select)
#     print(result)
