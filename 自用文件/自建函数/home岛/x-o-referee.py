# https://py.checkio.org/mission/x-o-referee/solve/

from typing import List, Tuple


# str = List[str]
def checkio(game_result: List[str]) -> str:
    global req
    L: List[Tuple[int, int, str]] = []
    P = 0
    for a in [0,1,2]:
        row = (a, game_result[a])
        for b in [0,1,2]:
            n = (b, a, row[1][b])
            L.append(n)
    # print(L)
    # print(('O' == L[1][2] and L[1][2] == L[4][2]) + ('O' == L[3][2] and L[3][2] == L[7][2]))

    for i in L:
        if i[0] == 0:
            if i[1] == 0:
                if (i[2] == L[1][2] and L[1][2] == L[2][2]) + (i[2] == L[3][2] and L[3][2] == L[6][2]) + (i[2] == L[4][2] and L[4][2] == L[8][2]) > 0:
                    req = i[2]
            elif i[1] == 1:
                if (i[2] == L[0][2] and L[0][2] == L[2][2]) + (i[2] == L[4][2] and L[4][2] == L[7][2]) > 0:
                    req = i[2]
            elif i[1] == 2:
                if (i[2] == L[0][2] and L[0][2] == L[1][2]) + (i[2] == L[5][2] and L[5][2] == L[8][2]) + (i[2] == L[4][2] and L[4][2] == L[6][2]) > 0:
                    req = i[2]
        elif i[0] == 1:
            if i[1] == 0:
                if (i[2] == L[0][2] and L[0][2] == L[6][2]) + (i[2] == L[4][2] and L[4][2] == L[5][2]) > 0:
                    req = i[2]
            elif i[1] == 1:
                if (i[2] == L[1][2] and L[1][2] == L[7][2]) + (i[2] == L[0][2] and L[0][2] == L[8][2]) + (i[2] == L[2][2] and L[2][2] == L[6][2]) + (i[2] == L[3][2] and L[3][2] == L[5][2]) > 0:
                    req = i[2]
            elif i[1] == 2:
                if (i[2] == L[2][2] and L[2][2] == L[8][2]) + (i[2] == L[3][2] and L[3][2] == L[4][2]) > 0:
                    req = i[2]
        elif i[0] == 2:
            if i[1] == 0:
                if (i[2] == L[0][2] and L[0][2] == L[3][2]) + (i[2] == L[2][2] and L[2][2] == L[4][2]) + (i[2] == L[7][2] and L[7][2] == L[8][2]) > 0:
                    req = i[2]
            elif i[1] == 1:
                if (i[2] == L[0][2] and L[0][2] == L[2][2]) + (i[2] == L[4][2] and L[4][2] == L[7][2]) > 0:
                    req = i[2]
            elif i[1] == 2:
                if (i[2] == L[2][2] and L[2][2] == L[5][2]) + (i[2] == L[0][2] and L[0][2] == L[4][2]) + (i[2] == L[6][2] == L[7][2]) > 0:
                    req = i[2]
    if '.' != req:
        return req
    return "D"

    # return "D" or "X" or "O"

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")