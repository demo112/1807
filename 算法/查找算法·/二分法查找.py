def binary(value, key):
    left = 0
    right = len(value) - 1
    # 循环遍历
    while left <= right:
        pass
        # 获取中间元素
        middle = (left + right) // 2
        if value[middle] == key:
            # 查找成功
            return middle
        elif value[middle] >= key:
            right = middle - 1
        else:
            # 如果中间值小于要查找的key值
            # 继续在右侧子表中查找
            left = middle + 1

    # 遍历完仍未找到
    return -1


values = [3, 9, 12, 25, 43, 45, 56, 67, 78, 89]
key = int(input("请输入查找的元素值"))

result = binary(values, key)
if result == -1:
    print("查找失败")
else:
    print("查找成功", result)
