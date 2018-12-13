from typing import List

def checkio(game_result: List[str]) -> str:
    a = 'D'
    if game_result[0][0] == game_result[0][1] == game_result[0][2]:
        a = game_result[0][0]
    if game_result[1][0] == game_result[1][1] == game_result[1][2]:
        a = game_result[1][0]
    if game_result[2][0] == game_result[2][1] == game_result[2][2]:
        a = game_result[2][0]
    if game_result[0][0] == game_result[1][0] == game_result[2][0]:
        a = game_result[0][0]
    if game_result[0][1] == game_result[1][1] == game_result[2][1]:
        a = game_result[0][1]
    if game_result[0][2] == game_result[1][2] == game_result[2][2]:
        a = game_result[0][2]
    if game_result[0][0] == game_result[1][1] == game_result[2][2]:
        a = game_result[0][0]
    if game_result[0][2] == game_result[1][1] == game_result[2][0]:
        a = game_result[0][2]

    if a != '.':
        return a

    return "D"


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
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")