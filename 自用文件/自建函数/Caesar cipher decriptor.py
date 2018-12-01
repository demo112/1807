def to_encrypt(text, delta):
    #replace this for solution
    new_text = ''
    for i in text:
        no = ord(i)
        if no in range(65, 123):
            print(ord(i))
            ii = chr(no + delta)
        elif no < 65:
            ii = chr(no + delta + 26)
        new_text += ii
        print(new_text)
    return new_text

if __name__ == '__main__':
    # print("Example:")
    # print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")