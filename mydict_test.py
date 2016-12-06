#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'Administrator'    # 单元测试
import unittest
from mydict import Dict


class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEquals(d.a, 1)
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d, Dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')

    def test_keyError(self):
        d = Dict()
        with self.assertRaises(KeyError):
           value = d['empty']     # 通过d['empty']访问不存在的key时，断言会抛出KeyError

    def test_attrError(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty      # 通过d.empty访问不存在的key时，我们期待抛出AttributeError

if __name__ == '__main__':
    unittest.main()

































