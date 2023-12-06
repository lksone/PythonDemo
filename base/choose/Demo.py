#!/usr/bin/python3
# -*- coding: utf-8 -*-

def match2():
    sum = 0
    for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        sum = sum + x
    print(sum)

# 如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，
# 可以生成一个整数序列，再通过list()函数可以转换为list。
# 比如range(5)生成的序列是从0开始小于5的整数
def match3():
    sum = 0
    for x in range(101):
        sum = sum + x
    print(sum)

def match4():
    sum = 0
    n = 99
    while n > 0:
        sum = sum + n
        n = n - 2
    print(sum)

if __name__ == '__main__':
    match4()