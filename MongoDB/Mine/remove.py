import pymongo
conn = pymongo.MongoClient('localhost', 27017)
dblist = conn.database_names()
db = 'test'
if db in dblist:
    mydb = conn.test
    mycol = mydb.class1
    # 删除内容
    mycol.remove({'name': '小孙'}, True)
    ret = mycol.delete_one({'name': '小孙'})
    print(ret.deleted_count)
    docs = mycol.find({}, {'_id': 0})
    for doc in docs:
        print(doc)
else:
    print("Not Found Collection", db)
conn.close()
