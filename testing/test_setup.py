#!/usr/local/bin python3
# -*- coding: utf-8 -*-
def setup_function():
    print("函数级别 setup ")
def teardown_function():
    print("函数级别 teardown")
def test_func1():
    print("测试 func1")
class TestDemo:
    def setup_class(self):
        print("类级别的setup")

    def teardown_class(self):
        print("类级别的teardown")

    def setup(self):
        print("方法级别的setup")

    def teardown(self):
        print("方法级别的tear")

    def test_demo1(self):
        print("testdemo1")

    def test_demo2(self):
        print("testdemo2")
