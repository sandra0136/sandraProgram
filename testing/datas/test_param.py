#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import pytest

# @pytest.fixture(params=adddatas,ids=myids)和@pytest.mark.parametrize('a,b,ex',adddatas,ids=myids)的效果一样
@pytest.fixture(params=[1, 2, 3], ids=['result1', 'result2', 'result3'])
def getdata(request):
    print(f"参数为：{request.param}")
    print("获取测试数据")


def test_case1(getdata):
    print("测试用例1")


def test_case2():
    print("测试用例2")
