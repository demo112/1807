import re

def checkio(expression):
    print(11)
    res = r"\w*(?P<left>(|[|{)\w*(?P<right>)|]|})\w*"
    res = r"\(\w+\)"
    rem = r"\w*(\w*)\w*"
    rel = r"\w*(\w*)\w*"
    objs = re.match(res, expression)
    i[1].upper()
    print(objs.group())
    # objm = re.findall(rem, expression)
    # objl = re.findall(rel, expression)


expression = "((5+3)*2+1)"
checkio(expression)
# These "asserts" using only for self-checking and not necessary for auto-testing

# if __name__ == '__main__':
    # assert checkio("((5+3)*2+1)") == True, "Simple"
    # assert checkio("{[(3+1)+2]+}") == True, "Different types"
    # assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    # assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    # assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    # assert checkio("2+3") == True, "No brackets, no problem"