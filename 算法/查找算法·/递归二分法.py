# 递归实现二分法查找
def binary(values, key, left, right):
    middle = (left + right) // 2
    if values[middle] == key:
        return middle
    elif left > right:
        return -1
    elif values[middle] > key:
        # 中间值大于key，在左侧子表中调用
        return binary(values, key, left, middle - 1)
    else:
        # 中间值小于key，在右侧子表中调用
        return binary(values, key, middle + 1, right)


values = [3, 9, 12, 25, 43, 45, 56, 67, 78, 89]

key = int(input("请输入查找的元素值"))

result = binary(values, key, 0, len(values) - 1)
if result == -1:
    print("查找失败")
else:
    print("查找成功", result)
