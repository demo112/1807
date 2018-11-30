import re
import sys


def get_port(input_port):
    f = open('1.txt')
# with open('1.txt') as f:
    while True:
        # 用空行分割各段
        data = ''
        for line in f:
            if line != '\n':
                data += line
            else:
                break
        # print(data)
        if not data:
            # return 'Not found the port'
            break
        # print('======================================================')
        # 匹配首单词
        PORT = re.match(r'\S+', data).group()
        # try:
        #     PORT = re.match(r'\S+', data).group()
        #     # print(PORT)
        # except Exception as e:
        #     print(e)
        #     continue
        if PORT == input_port:
            pattern = r'address is (\w{4}\.\w{4}\.\w{4})'
            # pattern = r'address is ((\d{1,3}\.){3}\d{1,3}/\d+|Unknown)'
            addr = re.search(pattern,data).group(1)
            # addr = re.search(pattern, data).group(1)
            return addr


if __name__ == '__main__':
    port = sys.argv[1]
    print(get_port(port))
