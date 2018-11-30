from pymongo import MongoClient

conn = MongoClient('localhost', 27017)

db = conn.stu

# 索引操作

# 为当前集合创建  索引
# index = myset.ensure_index('name')
# index2 = myset.ensure_index([('age', -1)])

# 为当前集合创建  复合索引
# index = myset.ensure_index([('name', 1), ('age', -1)])

# 为当前集合创建  唯一索引
# index = myset.ensure_index('name', name="Myindex", unique=True)

# 为当前集合创建  稀疏唯一索引
# index = myset.ensure_index('name', name="Myindex", unique=True, sparse=True)

# 删除所有索引
# myset.drop_indexes()

# 删除单个索引
# myset.drop_index('name_1')
# myset.drop_index('age_-1')
# print(index, index2)

# 获取当前集合的索引
# for i in myset.list_indexes():
#     print(i)


# 聚合操作
myset1 = db.class4
p = [
    {'$group': {'_id': '$皇帝', 'count': {'$sum':1}}},
    {'$match': {'count': {'$gt': 1}}}]


curcor = myset1.aggregate(p)

for i in curcor:
    print(i)

conn.close()
