#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import pytest
import yaml

# 读取yaml文件中的参数
with open('./test_cacl.yml') as a:
    muldatas = yaml.safe_load(a)['mul']
    muldata = muldatas['datas']
    mulmyid = muldatas['myid']

with open('./test_cacl.yml') as b:
    muldatas = yaml.safe_load(b)['mulf']
    muldata1 = muldatas['datas']
    mulmyid1 = muldatas['myid']


# 使用fixture进行参数化
@pytest.fixture(params=muldata, ids=mulmyid)
def get_muldatas(request):
    muldata = request.param
    print('muldata')
    return muldata


@pytest.fixture(params=muldata1, ids=mulmyid1)
def get_muldatas1(request):
    muldata1 = request.param
    print('muldata1')
    return muldata1


# 定义计算类
class TestCacla1():
    @pytest.mark.run(order=2)
    # 定义mul方法
    def test_mul(self, get_cacl, get_muldatas):
        result = get_cacl.mul(get_muldatas[0], get_muldatas[1])
        assert get_muldatas[2] == result

    @pytest.mark.run(order=1)
    # 定义mul小数方法
    def test_mul_float(self, get_cacl, get_muldatas1):
        result = get_cacl.mul(get_muldatas1[0], get_muldatas1[1])
        # 如果结果为小数,
        if isinstance(result, float):
            result = round(result, 6)

            # 断言
        assert get_muldatas1[2] == result