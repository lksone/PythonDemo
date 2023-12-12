#!/usr/bin/python3
# -*- coding: utf-8 -*-

#han

import functools

def f01(a, b, c):
    a2, b2, c2 = a + c, b * 2, c ** 2
    return a2, b2, c2

def put():
    x, y, z = f01(1, 2, 3)
    print('x, y, z', x, y, z)

    x, y, z = f01(x, y, z)
    print('x, y, z', x, y, z)


def add(a,b):
    return a + b

# lambda



if __name__ == '__main__':
    fun = lambda x, y: x * y
    print(fun(4, 5))  # 20
    # 生成新函数，添加的参数从左到右依次填充
    plus1 = functools.partial(add, 4)
    ret1 = plus1(6)  # 10
    ret2 = plus1(7)  # 11

    print(ret1)
    print(ret2)

    # lambda

    fun = lambda x, y: x * y
    print(fun(4, 5))  # 20
