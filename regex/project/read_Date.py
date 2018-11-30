import sys
import re

def main():
    # 从命令行获取服务端地址
    if len(sys.argv) < 3:
        print("argv is error")
        return
    PORT = sys.argv[1]

    pattern = PORT.encode() + r' is down'            # 匹配端口
    pattern_s = r'\n.+?'     # 匹配空行
    pattern_ip = r'Internet address is \d+.?\d+.?\d+.?\d+'     # 匹配地址
    f = open('1.txt')

    for line in f:
        regex = re.search(pattern,line)
        # 获取端口位置
        start_index = regex.pos
        # 获取终止位置 空行终止
        end_index = re.findall(pattern_s, line, start_index)