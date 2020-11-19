#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import os

import pytest
import yaml

from testwork.calc import Calculator

filedir = os.path.split(os.path.realpath(__file__))[0]
print(filedir)

with open(f"{filedir}/test_calc.yml") as f:
    # datas为dict
    datas = yaml.safe_load(f)
    add_datas = datas['add']['add_datas']
    add_ids = datas['add']['add_ids']
    sub_datas = datas['sub']['sub_datas']
    sub_ids = datas['sub']['sub_ids']
    dd_datas = datas['dd']['dd_datas']
    dd_ids = datas['dd']['dd_ids']


# 参数化1：@pytest.mark.parametrize('a,b,ex',add_datas,ids=add_ids)
# 参数化2：@pytest.fixture(params=,ids=)
@pytest.fixture(params=add_datas, ids=add_ids)
def get_adddatas(request):
    # request.param获取当前的参数
    data = request.param
    print(data)
    return data


@pytest.fixture(params=sub_datas, ids=sub_ids)
def get_subdatas(request):
    # request.param获取当前的参数
    data = request.param
    print(data)
    return data


# def get_dddatas(request):
#     data = request.param
#     print(data)
#     return data


class Testcalc():
    # 控制测试用例执行顺序
    @pytest.mark.run(order=2)
    # get_calc从conftest.py文件中获取
    def test_add(self, get_calc, get_adddatas):
        result = get_calc.add(get_adddatas[0], get_adddatas[1])
        assert get_adddatas[2] == result

    #
    @pytest.mark.run(order=1)
    def test_sub(self, get_calc, get_subdatas):
        result = get_calc.sub(get_subdatas[0], get_subdatas[1])
        assert get_subdatas[2] == result

    @pytest.mark.parametrize('a', dd_datas, ids=dd_ids)
    def test_dd(self, a):
        print(a)
