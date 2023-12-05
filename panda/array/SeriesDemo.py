#!/usr/bin/python3

import pandas as pd
import numpy as np

def create3():
    # 1、Series对象创建--空Series对象
    s1 = pd.Series()
    print(s1, type(s1), s1.dtype, s1.ndim)
    # 2、通过ndarray创建Series对象【或者是一个容器，字典时：key值为索引】
    ary1 = np.array([23, 45, 12, 34, 56])
    s2 = pd.Series(ary1)
    print(s2)

#创建索引标签
def createIndex():
    # 3、创建Series对象时，指定index行级索引标签
    ary1 = np.array([23, 45, 12, 34, 56])
    s3 = pd.Series(ary1, index=['zs', 'ls', 'ww', 'll', 'tq'])
    print(s3)


def create2():
    # 5、从标量创建一个系列
    s5 = pd.Series(5, index=[0, 1, 2, 3])
    print(s5)



if __name__ == '__main__':
    create2()

