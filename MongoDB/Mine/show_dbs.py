"""
1809pyMongo
"""
import pymongo

# 1.建立连接对象
conn = pymongo.MongoClient('localhost', 27017)

# 2.获取数据库列表
# dblist = conn.list_database_names()
dblist = conn.database_names()

# 3.遍历和打印
for db in dblist:
    print(db)

conn.close()
