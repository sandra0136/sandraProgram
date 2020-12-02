#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import pytest

# import sys
# sys.path.append('./..')
import yaml

from pythoncode.calc import Calculator

with open('./datas/calc.yml') as f:
    datas = yaml.safe_load(f)["add"]
    adddatas = datas["datas"]
    print(adddatas)
    myids = datas["myids"]
    print(myids)


class TestCalc:
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,ex', adddatas, ids=myids)
    def test_add(self, a, b, ex):
        # calc = Calculator()
        result = self.calc.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        # 断言
        assert ex == result

    @pytest.mark.add
    def test_add1(self):
        # calc = Calculator()
        result = self.calc.add(100, 100)
        # 断言
        assert 200 == result

    @pytest.mark.add
    def test_add2(self):
        # calc = Calculator()
        result = self.calc.add(0.1, 0.1)
        # 断言
        assert 0.2 == result

    @pytest.mark.parametrize("a,b,e", [
        (2, 1, 2),
        (100, 100, 1)
    ], ids=['int', 'bigint'])
    def test_div(self, a, b, e):
        # calc = Calculator()
        result = self.calc.div(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert e == result

    @pytest.mark.parametrize('a', [1, 2])
    @pytest.mark.parametrize('b', [2, 4])
    def test_div1(self, a, b):
        #  calc = Calculator()
        # result = self.calc.div(a, b)
        #  断言
        # assert 2 == result
        print(f"a={a},b={b}")
