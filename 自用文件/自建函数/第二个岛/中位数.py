from typing import List

def checkio(data: List[int]) -> [int, float]:
    data.sort()
    # print(data)
    l = int(len(data))
    # print(data, l)
    if l % 2 == 0:
        n1 = int(l / 2)
        n2 = int(l / 2 - 1)
        n = (data[n1] + data[n2]) / 2
        # print(data[n1], data[n2])
    else:
        n = int((l + 1) / 2) - 1
        n = data[n]

    # print(n)
    return n
    #replace this for solution
    #return data[0]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([1, 2, 3, 4, 5]))

    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("Coding complete? Click 'Check' to earn cool rewards!")
