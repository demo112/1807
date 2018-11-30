from pymongo import MongoClient
import gridfs
"""
    将文件以grid方案存放在数据库
    pymongo 实现 grids存储
    
    import gridfs
    
    GridFs()方法
    生成grid 数据库对象
"""
conn = MongoClient('localhost', 27017)
db = conn.grid
# 获取gridfs对象
fs = gridfs.GridFS(db)
f = open('mm.jpg', 'rb')
# 将内容写入到数据库
fs.put(f.read(), filename='mm.jpg')


conn.close()


