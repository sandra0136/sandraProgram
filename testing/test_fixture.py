#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import pytest


# 创建一个登录的fixture方法，yield关键字激活了fixture的teardown方法
@pytest.fixture(scope='module')
def login():
    print("登录操作")
    username = 'tom'
    password = '123456'
    # return [username, password]后面的代码无法执行，也就无法实现teardown的效果，必须用yield
    yield [username, password]
    print("退出登录")


# 测试用例1：需要提前登录
def test_case1(login):
    print(f"login username and password: {login}")
    print("测试用例1")


def test_case2():
    print("测试用例2")


def test_case3():
    print("测试用例3")
