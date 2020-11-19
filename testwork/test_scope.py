#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import pytest

from testwork.calc import Calculator

# fixture可以让方法调用更加灵活。
@pytest.fixture(scope='function')
def test_calc1():
    print("开始计算")
    calc = Calculator()
    # 这里的yield之后的代码效果类似与teardown方法。若是没有yield，则类似只实现了setup方法
    yield calc
    print("结束计算")


class Testscope():
    # 调用了test_cacl1方法(该方法被fixture装饰了)
    def test_add(self, test_calc1):
        print(test_calc1)
        print("test_add")
