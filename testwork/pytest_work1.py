#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import os

import pytest
import yaml

from pythoncode.calc import Calculator

filepath = os.path.split(os.path.realpath(__file__))[0]

with open(f"{filepath}/test_calc.yml") as f:
    # datas为字典
    datas = yaml.safe_load(f)
    adddic = datas['add']
    add_data = adddic['add_datas']
    add_ids = adddic['add_ids']
    subdic = datas['sub']
    sub_data = subdic['sub_datas']
    sub_ids = subdic['sub_ids']
    muldic = datas['mul']
    mul_data = muldic['mul_datas']
    mul_ids = muldic['mul_ids']
    divdic = datas['div']
    div_data = divdic['div_datas']
    div_ids = divdic['div_ids']
    dd_datas = datas['dd']['dd_datas']
    dd_ids = datas['dd']['dd_ids']
    print(type(add_ids))
    print(type(dd_ids))


class Testcalc():
    # 类级别的setup和teardown方法，只在类开始和结束时运行一次
    def setup_class(self):
        print("类级别setup开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("类级别teardown开始计算")

    def setup(self):
        print("方法级别setup开始")

    def teardown(self):
        print("方法级别teardown结束")

    # 设计加法测试用例
    # 参数化:
    @pytest.mark.parametrize('a,b,excp', add_data, ids=add_ids)
    def test_add(self, a, b, excp):
        result = self.calc.add(a, b)
        if isinstance(result, float):
            result = round(result, 3)
        assert excp == result

    # 注意：在yml文件中，
    @pytest.mark.parametrize('a,b,excp', sub_data, ids=sub_ids)
    def test_sub(self, a, b, excp):
        result = self.calc.sub(a, b)
        assert excp == result

    @pytest.mark.parametrize('a,ex', dd_datas, ids=dd_ids)
    def test_dd(self, a, ex):
        print(a)
        assert ex == a
