#!/usr/bin/python3
# -*- coding: utf-8 -*-
#元组

#特征：
#   元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表,不能被更新。
def demo():
    tuple = ('runoob', 786, 2.23, 'john', 70.2)
    print(tuple)
    print(tuple[0])
    print(tuple[0:3])
    print(tuple[2:])

    tinytuple = (123, 'john')
    print(tinytuple * 2)
    print(tuple + tinytuple)

#TypeError: 'tuple' object does not support item assignment
def demo2():
    tinytuple = (123, 'john')
    tinytuple[1] = 111


#这是元组，可以组成多维数组
def demo3():
    L = [
        ['Apple', 'Google', 'Microsoft'],
        ['Java', 'Python', 'Ruby', 'PHP'],
        ['Adam', 'Bart', 'Lisa']
    ]
    print(len(L))
    for a in L:
        for b in a:
            print(b)
        print("\n")
    print(L[0][0])
    print(L[1][1])
    print(L[2][2])
if __name__ == '__main__':
    demo3()