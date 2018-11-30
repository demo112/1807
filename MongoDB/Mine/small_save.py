from pymongo import MongoClient
import bson.binary
"""
    小文件存储方案，直接存储为二进制格式插入到数据库
    需要转化为mongoDB的二进制格式
    使用bson.binary.Binary()
    将bytes格式字串，转化为MongoDB的二进制存储格式    
"""
conn = MongoClient('localhost', 27017)
db = conn.image
myset = db.MM

f = open('mm.jpg', 'rb')
# 将图片内容转化为可存储的二进制格式
content = bson.binary.Binary(f.read())
# 插入到文档
myset.insert({'filename':'mm.jpg', 'data':content})

conn.close()