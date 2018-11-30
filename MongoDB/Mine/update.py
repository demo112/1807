import pymongo

conn = pymongo.MongoClient('localhost', 27017)
dblist = conn.database_names()
db = 'test'
if db in dblist:
    mydb = conn.test
    mycol = mydb.class1
    # 定义要修改的内容
    my_query = {'score': [100, 80, 98]}
    my_update = {'$set': {'name': '小陈', 'age': 10, 'sex': 'm', 'score': [100, 80, 98]}}
    ret = mycol.update_one(my_query, my_update,False, False)

    docs = mycol.find({}, {'_id': 0})
    for doc in docs:
        print(doc)
    print("修改笔数%s" % ret.modified_count)
else:
    print("Not Found Collection", db)
conn.close()
