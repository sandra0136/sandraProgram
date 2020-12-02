#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import pytest
import yaml

# 读取yaml文件中的数据
with open('./test_cacl.yml') as a:
    divdatas = yaml.safe_load(a)['div']
    divdata = divdatas['datas']
    divmyid = divdatas['myid']

# 读取yaml文件中的数据
with open('./test_cacl.yml') as b:
    divdatas1 = yaml.safe_load(b)['divzero']
    divdata1 = divdatas1['datas']
    divmyid1 = divdatas1['myid']


# 使用fixture起别名
@pytest.fixture(params=divdata, ids=divmyid)
# 定义获取数据的方法
def get_divdatdas(request):
    divdata = request.param
    print('divdata')
    return divdata


# 使用fixture起别名
@pytest.fixture(params=divdata1, ids=divmyid1)
# 定义获取数据的方法
def get_divdatdas1(request):
    divdata1 = request.param
    print('divdata1')
    return divdata1


# 定义计算类
from pytest_mode2.cacl import Calculator


# 定义计算类
class TestCacla1():
    # 控制测试用例执行顺序
    @pytest.mark.run(order=4)
    # 定义除法方法
    def test_div(self, get_cacl, get_divdatdas):
        result = get_cacl.div(get_divdatdas[0], get_divdatdas[1])
        # 断言
        assert get_divdatdas[2] == result

    # 控制测试用例执行顺序
    @pytest.mark.run(order=5)
    # 定义除法中被除外为0
    def test_div0(self, get_cacl, get_divdatdas1):
        # 判断被除数为0,打印被除数不能为0
        if get_divdatdas1[1] == 0:
            print('除数不能为0')
            return
        result = get_cacl.div(get_divdatdas1[0], get_divdatdas1[1])
        # 断言
        assert get_divdatdas1[2] == result