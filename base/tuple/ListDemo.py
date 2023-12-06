#!/usr/bin/python3
# -*- coding: utf-8 -*-


#列表
def demo():
    list = ['runoob', 786, 2.23, 'john', 70.2]
    tinylist = [123, 'john']

    print(list)  # 输出完整列表
    print(list[0])  # 输出列表的第一个元素
    print(list[1:3]) # 输出第二个至第三个元素
    print(list[2:]) # 输出从第三个开始至列表末尾的所有元素
    print(tinylist * 2) # 输出列表两次
    print(list + tinylist)  # 打印组合的列表

def demo2():
    list = ['runoob', 786, 2.23, 'john', 70.2]

    print(list[0])
    print(list[-1])

    #添加
    list.append(42342)
    print(list)

    #角标为1的地方插入
    list.insert(1,"fdsf")
    print(list)


    list.clear()
    print(list)
    print(len(list))

def demo3():
    list = ['runoob', 786, 2.23, 'john', 70.2]
    print(list)
    #将最后数据推出
    list.pop()
    print(list)
    #推出角标为1的
    list.pop(1)
    print(list)

    l1 = ['wangh', 'kongl', 'wanghjy']

    l1.reverse()
    l1.sort()
    print(l1)


    for name in l1:
        print(name)

    l2 = range(10)
    for i in l2:
        print(i)

if __name__ == '__main__':
    demo3()
