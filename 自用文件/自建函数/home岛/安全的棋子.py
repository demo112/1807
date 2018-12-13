def safe_pawns(pawns: set) -> int:
    global safe_row
    pawns = [x for x in pawns]
    print(pawns)
    n = 0
    for i in pawns:
        line = i[0]
        row = i[1]
        # print(line, row)
        if 1 < int(row) < 9:
            safe_row = int(row) - 1
        elif int(row) == 1:
            continue

        if 'a' < line < 'h':
            safe_line1 = chr(ord(line) + 1)
            safe_line2 = chr(ord(line) - 1)
            point1 = safe_line1 + str(safe_row)
            point2 = safe_line2 + str(safe_row)
            if point1 in pawns:
                n += 1
            elif point2 in pawns:
                n += 1

        elif line == 'a':
            safe_line = ord(line) + 1
            print(chr(safe_line))
            point = chr(safe_line) + str(safe_row)
            if point in pawns:
                n += 1

        elif line == 'h':
            safe_line = ord(line) - 1
            print(chr(safe_line))
            point = chr(safe_line) + str(safe_row)
            if point in pawns:
                n += 1
    print(n, i)
    return n


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    assert safe_pawns(["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"]) == 7
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
