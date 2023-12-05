#!/usr/bin/python3

import json
#创建一个类对象，如何使用类对象
class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

        # PEP 8要求标识符的名字用全小写多个单词用下划线连接
        # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)

    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)



if __name__ == '__main__':
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('骆昊', 38)
    # 给对象发study消息
    stu1.study('Python程序设计')
    # 给对象发watch_av消息
    stu1.watch_movie()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_movie()


    #json.dumps方法不能对自定义对象直接序列化,首先把自定义对象转换成字典
    print(json.dumps(stu1.__dict__))
    print(type(stu1))