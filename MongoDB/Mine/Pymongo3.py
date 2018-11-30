from random import randint
from pymongo import MongoClient

conn = MongoClient('localhost', 27017)

db = conn.grade

myset = db.Class

# curcor = myset.find()
# for i in curcor:
#     myset.update({'_id': i['_id']},
#                  {'$set': {'$score':
#                                {'Chinese': randint(80, 99),
#                                 'math': randint(80, 99),
#                                 'english': randint(80, 99)
#                                 }}})
#

l1 = [{}]

curcor = myset.aggregate([{'$group':{'_id':'$sex', 'num':{'$sum':1}}}])

for i in curcor:
    print(i)



conn.close()
