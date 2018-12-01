import re
def to_encrypt(text, delta):
    #replace this for solution
    text = text.lower()
    new_text = ''
    # pattern = r'\b\s+'
    # regex = re.split(pattern, text)
    # print(regex)
    for i in text:
        no = ord(i)
        if no == 32:
            ii = i
        elif (no + delta) < 97:
            ii = chr(no + delta + 26)
        elif (no + delta) > 122:
            ii = chr(no + delta - 26)
        elif no in range(97, 123):
            ii = chr(no + delta)
        new_text += ii

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


def to_encrypt(text, delta):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for ch in text:
        if ch == " ":
            encrypted += " "
        else:
            pos = alphabet.index(ch)
            encrypted += alphabet[(pos+delta)%26]
    print (encrypted)
    return encrypted

if __name__ == '__main__':
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")