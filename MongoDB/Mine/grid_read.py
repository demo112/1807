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
# 从数据库中获取
files = fs.find()
for i in files:
    if i.filename == 'mm.jpg':
        with open(i.filename, 'wb') as f:
            # 读取文件
            data = i.read()
            # 写入本地
            f.write(data)

conn.close()
