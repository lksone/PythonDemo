#!/usr/bin/python3
import os
import threading
import cProfile


#定义全局变量
file_path="C:\\Users\\Administrator\\Desktop\\升级脚本\\mysql.rar"
num_threads = 4
block_size=1024


def read_file(thread_id,start_pos,end_pos,result):
    with open(file_path,"rb") as file:
        file.seek(start_pos)
        data = file.read(end_pos-start_pos)
        result[thread_id] = data


def main():
    #获取文件大小
    file_size = os.path.getsize(file_path)
    print("文件大小为：%s"% file_size)
    #计算每个线程要读取的block 的大小
    block_size = file_size // num_threads
    print("block 的大小：%s" % block_size)
    #创建缓存存放结果列表
    result = [None] * num_threads;

    #创建线程
    threads = []
    #线程循环，通过
    for i in range(num_threads):
        #文件开始的位置
        start_pos = i * block_size
        # 最后一个线程读取的结束位置要调整为文件的末尾
        end_pos = start_pos + block_size if i < num_threads - 1 else file_size


        #线程执行，目标方法
        thread = threading.Thread(target=read_file, args=(i, start_pos, end_pos, result))
        print("线程：%s,开始读取startPos:%s ,结束：endOps=%s" %(thread.name,start_pos,end_pos))
        threads.append(thread)
        thread.start()

        # 等待所有线程完成读取操作
    for thread in threads:
        thread.join()
    # 按照线程的读取顺序将每个线程读取的数据按顺序合并到一个文件中或在内存中进行相应的处理
    with open("merged_file", "wb") as merged_file:
        for data in result:
            merged_file.write(data)

if __name__ == "__main__":
    main()
    print(cProfile.run("main()"))