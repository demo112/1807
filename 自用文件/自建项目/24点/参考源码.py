#coding:utf-8
from __future__ import division
from node import node

"""
    来源网页
    http://www.cnblogs.com/junyuhuang/p/5105693.html?utm_source=tuicool&utm_medium=referral
"""
def calculate(nums):
    nums_possible = list_result(nums)
    operators_possible = list_result(['+','-','*','÷'])
    goods_noods = []
    for nums in nums_possible:
        for op in operators_possible:
            node = one_expression_tree(op, nums)
            if cal_tree(node) == 24:
                goods_noods.append(node)
            node = two_expression_tree(op, nums)
            if cal_tree(node) == 24:
                goods_noods.append(node)
    map(lambda node: print_expression_tree(node), goods_noods)




def cal_tree(node):
    if node.left is None:
        return node.val
    return cal(cal_tree(node.left), cal_tree(node.right), node.val)


#根据两个数和一个符号，计算值
def cal(a, b, operator):
    return operator == '+' and float(a) + float(b) or operator == '-' and float(a) - float(b) or operator == '*' and  float(a) * float(b) or operator == '÷' and float(a)/float(b)

def one_expression_tree(operators, operands):
    root_node = Node(operators[0])
    operator1 = Node(operators[1])
    operator2 = Node(operators[2])
    operand0 = Node(operands[0])
    operand1 = Node(operands[1])
    operand2 = Node(operands[2])
    operand3 = Node(operands[3])
    root_node.left = operator1
    root_node.right =operand0
    operator1.left = operator2
    operator1.right = operand1
    operator2.left = operand2
    operator2.right = operand3
    return root_node

def two_expression_tree(operators, operands):
    root_node = Node(operators[0])
    operator1 = Node(operators[1])
    operator2 = Node(operators[2])
    operand0 = Node(operands[0])
    operand1 = Node(operands[1])
    operand2 = Node(operands[2])
    operand3 = Node(operands[3])
    root_node.left = operator1
    root_node.right =operator2
    operator1.left = operand0
    operator1.right = operand1
    operator2.left = operand2
    operator2.right = operand3
    return root_node

#返回一个列表的全排列的列表集合
def list_result(l):
    if len(l) == 1:
        return [l]
    all_result = []
    for index,item in enumerate(l):
        r = list_result(l[0:index] + l[index+1:])
        map(lambda x : x.append(item),r)
        all_result.extend(r)
    return all_result

def print_expression_tree(root):
    print_node(root)
    print(' = 24')

def print_node(node):
    if node is None :
        return
    if node.left is None and node.right is None:
        print(node.val,)
    else:
        print('('),
        print_node(node.left)
        print(node.val,)
        print_node(node.right)
        print(')'),

if __name__ == '__main__':
    calculate([2,3,4,6])