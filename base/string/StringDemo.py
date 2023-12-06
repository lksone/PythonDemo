#!/usr/bin/python3




def demo1():
    s1 = 'hello, world!'
    s2 = "hello, world!"
    # 以三个双引号或单引号开头的字符串可以折行，换行，使用“”“
    s3 = """
    hello, 
    world!
    """
    print(s1, s2, s3, end='')

    #取'
    s1 = '\'hello, world!\''
    #取斜杠
    s2 = '\n\\hello, world!\\\n'
    print(s1, s2, end='')

    s1 = '\141\142\143\x61\x62\x63'
    s2 = '\u9a86\u660a'
    print(s1, s2)

###Python为字符串类型提供了非常丰富的运算符，我们可以使用+运算符来实现字符串的拼接，
# 可以使用*运算符来重复一个字符串的内容，可以使用in和not in来判断一个字符串是否包含另外一个字符串（成员运算），
# 我们也可以用[]和[:]运算符从字符串取出某个字符或某些字符（切片运算），
# 代码如下所示。###
def demo2():
    s1 = 'hello ' * 3
    print(s1)  # hello hello hello

    s2 = 'world'
    s1 += s2
    print(s1)  # hello hello hello world
    #判断是否存在
    print('ll' in s1)  # True
    print('good' in s1)  # False


#截取字符
def demo3():
    str2 = 'abc123456'
    # 从字符串中取出指定位置的字符(下标运算)
    print(str2[2])  # c

    # 字符串切片(从指定的开始索引到指定的结束索引)
    print(str2[2:5])  # c12
    #下标为2后面所有的字符
    print(str2[2:])  # c123456
    #从第2个字符开始，每隔2个字符获取
    print(str2[2::2])  # c246
    #每2个获取一次
    print(str2[::2])  # ac246
    #倒序获取
    print(str2[::-1])  # 654321cba
    print(str2[-3:-1])  # 45


def demo4():
    str2 = 'abc123456'
    print(str2[2])

### 常用方法String
def demo5():
    s1 = '   fdsfd  saa   ';
    #去除左边空白
    print(s1.lstrip())
    #去除右边空白
    print(s1.rstrip())

    print(s1)
    #去左右除空白
    print(s1.strip())

    s2 = ',,,abc,,,'
    print(s2.strip(','))  # 去除左右指定字符
    print(s2.lstrip(','))  # 去除左边指定字符
    print(s2.rstrip(','))  # 去除右边指定字符

    l1 = ['first', 'second', 'three']
    print(s1.join(l1))  # 在参数列表项之间插入本字符串，若只有1项，则不插入
    print(s1.find('b'))  # 查找字符，返回第一次找到时的索引
    print(type(s1.find('b')))

    #数据比较
    # 字符串比较
    print("-----------------------------字符串比较-----------------------------")
    print('a' < 'b')  # True
    print('ab' > 'b')  # False
    print('ab' < 'b')
    print('ab' > 'aa')  # True
    print('aa' == 'aa')  # True

    string_1 = "Hello"
    string_2 = "Hello"

    print("Is string_1 != string_2?")

    # comapare not equality between string1 and string2,没有地址的概念
    print(string_1 != string_2)
    print(string_1 == string_2)

    #获取字符串长度
    print(len("1231312"))

    #字符串大小
    # 字符串转换
    s1 = 'aBcDeF hIjKlM'
    # 转换为大写
    print(s1.upper())
    # 转换为小写
    print(s1.lower())
    # 大小写互转
    print(s1.swapcase())
    # 首字母大写，其余字符转为小写
    print(s1.capitalize())

    # 字符串分割
    s1 = 'abc,def,ghi'
    # 按指定字符分割，返回列表
    print(s1.split(','))
    pass


if __name__ == '__main__':
    demo5()