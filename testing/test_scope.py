#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import pytest


# 从哪里开始传递，从哪里开始生效；必须传递一次，才有效。
@pytest.fixture(scope='module')
def connectDB():
    print("连接数据库操作")
    yield
    print("断开数据库连接")


class TestDemo:
    def test_a(self):
        print("测试用例a")

    def test_b(self, connectDB):
        print("测试用例b")

    def test_c(self):
        print("测试用例c")
