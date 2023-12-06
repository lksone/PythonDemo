#!/usr/bin/python3
# -*- coding: utf-8 -*-

#字典字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合
def demo():
    dict = {}
    dict['one'] = "This is one"
    dict[2] = "This is two"
    tinydict = {'name': 'runoob', 'code': 6734, 'dept': 'sales'}
    print(tinydict)
    print(dict[2])
    print(dict['one'])
    print(tinydict.values())
    print(tinydict.keys())
    print(dict)

def demo2():
    tinydict = {'name': 'runoob', 'code': 6734, 'dept': 'sales'}
    print(tinydict.get('name1'))
    b =  tinydict.get('name1')
    if(b is None):
        print("fdsfds")

    print(type(b))

if __name__ == '__main__':
    demo2()