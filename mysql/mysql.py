#!/usr/bin/python3

import pymysql
import pandas as pd

import json

#连接数据库
def connect():
    print("开始连接数据库------------------------")
    return pymysql.connect(host='127.0.0.1', port=3306, user='root', password='12345678', database='ztjk-xw')

#查询一条数据
def selectOne(sql):
    db = connect()
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用游标执行
    result = cursor.execute(sql)
    c = []
    # 查询一条数据，数据返回的是一个元组
    table_head = cursor.fetchone()
    # 取表头即索引 sname，ssex之类
    count = 0
    for abb in table_head:
        c.append(abb)
    print(c)

#查询一条数据
def selectAll(sql):
    db = connect()
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用游标执行
    result = cursor.execute(sql)
    c = []
    # 查询一条数据，数据返回的是一个元组
    table_head = cursor.fetchall()
    # 取表头即索引 sname，ssex之类
    count = 0
    #多条数据多循环一次
    for abb in table_head:
        for a in abb:
            c.append(a)
    print(c)

#查询指定的数据库列名列名
def selectHead(sql):
    db = connect()
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用游标执行
    result = cursor.execute(sql)
    c = []
    # 查询一条数据，数据返回的是一个元组
    table_head = cursor.fetchall()
    # 多条数据多循环一次
    for abb in table_head:
        for a in abb:
            c.append(a)
    print(c)

#将数据写入到excel cvs
def selectPD(sql):
    db = connect()
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用游标执行
    result = cursor.execute(sql)
    c = []
    # 查询一条数据，数据返回的是一个元组
    table_head = cursor.fetchall()
    # 取表头即索引 sname，ssex之类
    count = 0
    #多条数据多循环一次
    jj = json.dumps(table_head)
    print(jj)
    #pd.DataFrame(table_head.__dict__)

if __name__ == '__main__':
    #查询sql
    sql = "select * from task_info where task_id = '019dc4feb6aa4c0aa1b90eaf326417f9'"

    #查询数据库列表名称
    #sqlHeader = "SELECT COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = 'task_info'";
    selectPD(sql)