from pymongo import MongoClient

# 创建数据库连接
conn = MongoClient('localhost', 27017)

# 创建数据库对象
db = conn.stu

# 创建集合对象
my_set = db.class4
my_set1 = db.class0


# 数据操作
# my_set.insert({'name': '张铁林', '皇帝': '乾隆'})
# my_set.insert([
#                 {'name': '张国立', '皇帝': '康熙'},
#                 {'name': '陈道明', '皇帝': '康熙'}
#             ])
# my_set.insert_many([
#                     {'name': '唐国强', '皇帝': '雍正'},
#                     {'name': '陈建斌', '皇帝': '雍正'}])

# my_set.insert_one({'name': '郑少秋', '皇帝': '乾隆'})
# my_set.save({'_id': 1, 'name':'聂远', '皇帝':'乾隆'})
# my_set.save({'_id': 1, 'name':'吴奇隆', '皇帝':'雍正'})
# print(dir(my_set))

# 操作符
curcor = my_set1.find({'age': {'$gt': 18}}, {'_id': 0})
# curcor = my_set1.find({'age': {'$gt': 18}}, {'_id': 0})

# for i in curcor:
#     print(i)

# 获取下一跳数据
# print(curcor.next())
# print(curcor.next())
# for i in curcor.sort([('age',1), ('name',-1)])\
#                 .limit(5).skip(1):
#     print(i)

# query = {'$or': [{'age': {'$lt': 19}}, {'sex': 'w'}]}
# curcor = my_set1.find(query, {'_id': 0})
# for i in curcor:
#     print(i)

# 查找
# curcor = my_set.find({},{'_id':0})
# # print(curcor)
#
# for i in curcor:
#     # print(i)
#     print(i['name'],'----',i['皇帝'])
# curcor = my_set.find_one({},{'_id':0})
# print(curcor)

# 修改
# my_set1.update({'name': 'Jame'}, {'$unset': {'tel': ''}})
# my_set1.update({'name': 'Jame'}, {'$set': {'age': 21}}, multi=True)

# 插入
# my_set.update({'name': "张家辉"}, {'$set':{"皇帝": '咸丰'}}, upsert=True)
# my_set.update_many({'皇帝': "咸丰"}, {'$set':{"name": '张家辉'}})
# my_set.update_one({'皇帝': "康熙"}, {'$set':{"KingName": '玄烨'}})

# 删除
# my_set.remove({'皇帝':'四爷'}, multi=True)
# my_set.remove({'皇帝':'咸丰'}, multi=False)
# my_set1.remove({'gender': {'$exists':False}})
# 关闭链接
conn.close()
