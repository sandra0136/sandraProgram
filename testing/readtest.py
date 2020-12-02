#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import pytest
import yaml

from pythoncode.calc import Calculator

with open('./datas/ca.yml') as f:
    datas = yaml.safe_load(f)['data']
    adddata = datas['adddata']
    divdata = datas['divdata']
    addids = datas['dataids']['addid']
    divids = datas['dataids']['divid']
    print(adddata)
    print(divdata)
    print(addids)
    print(divids)


@pytest.fixture(params=adddata, ids=addids)
def get_datas(request):
    print(request.param)
    return request.param


class TestCaseDemo:
    def setup_class(self):
        self.ca = Calculator()

    def setup(self):
        print("开始测试用例")

    def teardown(self):
        print("结束测试用例")

    @pytest.mark.addUseCase
    @pytest.mark.parametrize("a,b,ex", adddata, ids=addids)
    def test_add(self, a, b, ex):
        result = self.ca.add(a, b)
        assert ex == result

    def test_add1(self, get_datas):
        result = self.ca.add(get_datas[0], get_datas[1])
        assert get_datas[2] == result

    # 在命令行执行的时候可以用，选则执行哪些东西
    @pytest.mark.divUseCase
    # ids是针对一个"单元"下的测试用例进行编号
    @pytest.mark.parametrize("a,b,ex", divdata, ids=divids)
    def test_div(self, a, b, ex):
        result = self.ca.div(a, b)
        if isinstance(result, float):
            result = round(result, 3)
        assert ex == result
