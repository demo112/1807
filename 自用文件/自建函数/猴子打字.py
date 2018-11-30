import re
def count_words(text: str, words: set) -> int:
    a = 0
    for i in words:
        pattern = r"%s" % i
        regex = re.compile(pattern, re.I)
        n = regex.findall(text)
        if n:
            a += 1
    print(a)
    return a


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
