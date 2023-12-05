#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py
import sys;

if __name__ == '__main__':
    if True:
        print("这是正确的判断")
    else:
        print("这是错误的判断")
    print("无论如何都输出参数")
  #  raw_input("任意按下enter....\n")


    x = 'runoob';
    sys.stdout.write(x + '\n')
    sys.stdout.write(x + '\n')

    #重复值赋值
    a=b=c=1
    print(a,b,c)
    print(b)
    print(c)
    #多数据赋值
    counter = 1000
    print(counter)