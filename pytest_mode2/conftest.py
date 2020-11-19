#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import pytest

from pytest_mode2.cacl import Calculator


@pytest.fixture(scope='module')
def get_calc():
    print("获取计算机实例")
    calc = Calculator
    return calc


# 更改编码
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: list["Item"]
) -> None:
    print("items")
    print(items)
    # items.reverse() #翻转items的顺序

    # 遍历一下item
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


# 注册一个命令行参数env，定义分组hogwarts ,将参数 env放在hogwards分组下
def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")  # group将下面所有的option都展示在这个group下
    mygroup.addoption("--env",
                      default='test',  # 默认值
                      dest='env',  # 存储的变量
                      help='set your run env'  # 参数说明
                      )
    mygroup.addoption("--des",
                      default='dev',  # 默认值
                      dest='dev',  # 存储的变量
                      help='set your param'  # 参数说明
                      )
    mygroup.addoption("--dem",
                      default='st',  # 默认值
                      dest='st',  # 存储的变量
                      help='set your param'  # 参数说明
                      )


# env默认值是test,表示测试环境
@pytest.fixture(scope='session')
def cmdoption(request):
    return request.config.getoption("--env", default='test')
