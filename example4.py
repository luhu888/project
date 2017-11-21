#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'Administrator'


class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

Student('LuHu')
print callable(Student)














































































