

def insert(values):
    global P
    if len(values) == 1:
        return values
    for i in range(1, len(values)):
        t = values[i]
        for j in range(i - 1, -1, -1):
            # 从当前无序数据i的前一个开始
            # 遍历到0为止
            if values[j] > t:
                values[j + 1] = values[j]
                P = j
                # break
            else:
                P =  j + 1
                break
        values[P] = t
    return values


if __name__ == "__main__":
    values = [23, 45, 2, 67, 34, 9, 86, 39, 52, 73, 19, 98, 27]
    # values = [2, 4, 1, 3]
    L = insert(values)
    print(L)
