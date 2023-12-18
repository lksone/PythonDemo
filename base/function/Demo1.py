#!/usr/bin/python3
# -*- coding: utf-8 -*-

def getAnswer(answerNumber):
    if(answerNumber == 1):
        return 1;
    elif(answerNumber==2):
        return '2'
    else:
        print('error')
if __name__ == '__main__':
   a = getAnswer(2)
   print(a)
   print(type(a))

   b = 1
   a = '1'

   print(a==b)