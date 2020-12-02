#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import pytest
import yaml

from pytest_mode2.cacl import Calculator

# 打开test_cacl.yml文件,读取数据
with open('./test_cacl.yml') as a:
    adddatas = yaml.safe_load(a)['add']
    adddata = adddatas['datas']
    addmyid = adddatas['myid']

with open('./test_cacl.yml') as b:
    adddatas = yaml.safe_load(b)['addstr']
    strdata = adddatas['datas']
    strmyid = adddatas['myid']


# 使用fix给add参数起别名
@pytest.fixture(params=adddata, ids=addmyid)
def get_adddatas(request):
    adddata = request.param
    print('adddata')
    return adddata


# 使用fix给addstr参数起别名
@pytest.fixture(params=strdata, ids=strmyid)
def get_adddatas1(request):
    strdata = request.param
    print('strdata')
    return strdata


# 定义计算类

class TestCacla():
    @pytest.mark.run(order=1)
    # 定义add方法
    def test_add(self, get_cacl, get_adddatas):
        result = get_cacl.add(get_adddatas[0], get_adddatas[1])
        # 判断结果为小数时取小数点后两位
        if isinstance(result, float):
            result = round(result, 2)
            # 断言
        assert get_adddatas[2] == result

    @pytest.mark.run(order=2)
    # 定义add异常方法
    def test_add_str(self, get_cacl, get_adddatas1):
        # 判断结果参数有str的类型
        if isinstance(get_adddatas1[0], str) or isinstance(get_adddatas1[1], str):
            print('不支持字符串')
            return
        else:
            print('get_adddatas1[0]')
            print('get_adddatas1[1]')
            print('请输入正确的类型')
        result = get_cacl.add(get_adddatas1[0], get_adddatas1[1])
        # 断言
        assert get_adddatas1[2] == result