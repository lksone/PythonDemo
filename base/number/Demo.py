#!/usr/bin/python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    numser1 = 1
    print(numser1)
    print(type(numser1))
    #long 类型只存在于 Python2.X 版本中，在 2.2 以后的版本中，int 类型数据溢出后会自动转为long类型。在 Python3.X 版本中 long 类型被移除，使用 int 替代。
    numser2 = 51924361123131231231231231111111111111111111111111111111111111111
    print(numser2)
    print(type(numser2))

    #浮点数
    numser3 = 12.12
    print(numser3)
    print(type(numser3))

    #复数
    numser4 = 3.12j
    print(numser4)
    print(type(numser4))