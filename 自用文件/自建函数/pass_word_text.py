def checkio(str):
    lst = list(str.strip(''))
    # print(lst)
    a = b = c = 0
    for i in lst:
        n = ord(i)
        # print(n)
        if len(lst) >= 10:
            if 48 <= n <= 57:
                a += 1
            if 65<= n <= 90:
                b += 1
            if 97<= n <= 122:
                c += 1
            # print('a =', a * b * c)
    if a * b * c > 0:
        return True
    else:
        return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")