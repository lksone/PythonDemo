import pymysql,random
import time

import csv


def insert(filename):
    # 连接数据库  host - 主机名 user - 用户名 password - 密码 database - 数据库名 port -端口
    db = pymysql.connect(host="127.0.0.1", user="root", password="123456", database="test", port=3306,local_infile=True)
    cursor = db.cursor()

    #导入数据
    sql = '''
    LOAD DATA LOCAL INFILE '{}' INTO TABLE test
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\r\n'
    IGNORE 1 LINES
    (time, name)
    '''.format(filename)
    cursor.execute(sql)
    db.commit()
    db.close()

# 生成csv文件
def createCSV(filename, num):
    fp = open("test/test.txt", "r", encoding="UTF-8")
    names = fp.read().split('、')
    headers = ['time', 'name']
    rows = []
    for i in range(num):
        index_name = random.randint(0, len(names) - 1)
        year = random.randint(2015, 2019)
        month = random.randint(1, 12)
        day = random.randint(1, 31)
        name = names[index_name]
        time = ''.join([str(year), '/', str(month), '/', str(day)])
        rows.append((time, name))
    with open(filename, 'w', encoding='utf8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

if __name__ == "__main__":
    # 生成csv测试文件
    createCSV("test/test.csv", 1000000)
    starttime = time.time()
    print("开始插入......")
    insert("test/test.csv")
    endtime = time.time()  # 结束记录
    print("插入成功,总计耗时", endtime - starttime)
