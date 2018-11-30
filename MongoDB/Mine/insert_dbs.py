import pymongo
conn = pymongo.MongoClient('localhost', 27017)
dblist = conn.database_names()
db = 'test'
if db in dblist:
    mydb = conn.test
    mycol = mydb.class1
    # 定义要插入的内容
    mydict = {'name': '小孙',
              'age': 10,
              'score': [90, 98, 97]
              }
    ret = mycol.insert_one(mydict)
    print(ret.inserted_id)
    docs = mycol.find({}, {'_id': 0})
    for doc in docs:
        print(doc)
else:
    print("Not Found Collection", db)
conn.close()
