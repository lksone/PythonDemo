#!/usr/bin/python3
#pip install pymysql  #安装读取数据库的库
import pandas as pd
import numpy as np
import pymysql
from sqlalchemy import create_engine
import time
from datetime import date



def connect():
    con = pymysql.connect(host="127.0.0.1", user="root", port=3306,password="12345678", db="ztjk-xw")
    # 读取sql
    data_sql = pd.read_sql("select * from task_info where task_type=4", con)

    sqlHeader = "SELECT COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = 'task_info'";

    data_header = pd.read_sql(sqlHeader, con)
    s = pd.DataFrame(data=data_sql.values,columns=data_header.values)
    print(s)

def connect2():
    DB_USER = 'root'
    DB_PASS = '12345678'
    DB_HOST = '127.0.0.1'
    DB_PORT = '3306'
    DATABASE = 'ztjk-xw'
    connect_info = 'mysql+pymysql://root:12345678@127.0.0.1:3306/ztjk-xw?charset=utf8';

    engine = create_engine(connect_info)
    # sql 命令
    sql_cmd = "SELECT task_id,task_type,barcode,barcode_text,create_date as time1 FROM task_info order by create_date"
    df = pd.read_sql_query(sql=sql_cmd, con=engine)
    df.columns = ['任务ID', '任务类型', '条码', '条码文本','创建时间']
    df.to_excel('a.xlsx', index=False)
    print(df)

if __name__ == '__main__':
    connect2()