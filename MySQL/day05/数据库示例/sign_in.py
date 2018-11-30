from MysqlPython import MysqlHelp
from hashlib import sha1


username = input('请输入用户名')
password = input('请输入密码')


# 给password加密
s1 = sha1()     # 创建sha1的对象
s1.update(password.encode('utf-8'))      # 转码
password2 = s1.hexdigest()                # 返回16进制加密结果
# print(password2)

# 和数据库中表记录进行匹配
mysql = MysqlHelp('db4')
sql_select = 'select password from user where username=%s'
result = mysql.get_all(sql_select, [username])
# print(result)

if len(result) == 0:
    print('用户名不存在')
elif password2 == result[0][0]:
    print('登陆成功')
else:
    print('密码错误')
