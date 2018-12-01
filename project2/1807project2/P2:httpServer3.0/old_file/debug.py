import sys
import pdb
import http.server
from http.server import HTTPServer, BaseHTTPRquestHandler



def add(n1=0, n2=0):
    return int(n1) + int(n2)


def sub(n1=0, n2=0):
    return int(n1) - int(n2)


def main():
    print(sys.argv)
    pdb.set_trace()
    a = add(sys.argv[1], sys.argv[2])
    print(a)
    s = sub(sys.argv[1], sys.argv[2])
    print(s)


if __name__ == '__main__':
    main()
