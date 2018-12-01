from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    l = len(elements)
    for i in range(l - 1):
        a = elements[i]
        b = elements[i + 1]
        if b == '':
            return True
        elif a is b:
            return True
        else:
            return False

    return True


if __name__ == '__main__':
    # print("Example:")
    # print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")