#!/usr/bin/python3
# -*- coding: utf-8 -*-


class myclass(object):
    def __init__(self):
        self._param1 = None
        self._param2 = None

    def getParam1(self):
        print('getParam1:%s'%self._param1)
        return self._param1;