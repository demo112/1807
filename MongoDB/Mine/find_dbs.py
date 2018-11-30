import pymongo
conn = pymongo.MongoClient('localhost', 27017)
# noinspection PyDeprecation
dblist = conn.database_names()

# 判断库是否存在
db = 'test'
if db in dblist:
    # 获取数据库对象
    mydb = conn.test

    # 获取集合对象
    # mydb = conn['test']
    mycol = mydb.class1

    # docs = mycol.find({}, {'_id': 0})
    docs = mycol.find({'sex':'w'}, {'_id': 0})
    for doc in docs:
        print(doc)
else:
    print("Not Found Collection", db)
conn.close()
