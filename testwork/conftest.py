#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import pytest

from testwork.calc import Calculator


# 使用fixture方法，将scope设置为模块类
@pytest.fixture(scope='module')
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc


@pytest.fixture(scope='function')
def get_calc1():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")
