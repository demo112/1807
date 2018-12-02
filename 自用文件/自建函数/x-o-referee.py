# https://py.checkio.org/mission/x-o-referee/solve/

from typing import List
# str = List[str]
def checkio(game_result: List[str]) -> str:
    L = []
    P = 0
    for a in [0,1,2]:
        row = (a, game_result[a])
        for b in [0,1,2]:
            n = (b, a, row[1][b])
            L.append(n)

    for i in L:
        list = filter(a[0] == "0", L)
        print(list)

    # return "D" or "X" or "O"

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    # assert checkio([
    #     "OOX",
    #     "XXO",
    #     "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")