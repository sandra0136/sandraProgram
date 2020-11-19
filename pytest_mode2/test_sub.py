#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import pytest

import yaml

# 读取yaml文件中的参数
with open('./test_cacl.yml') as a:
    subdatas = yaml.safe_load(a)['sub']
    subdata = subdatas['datas']
    submyid = subdatas['myid']


# 参数化
@pytest.fixture(params=subdata, ids=submyid)
def get_subdatas(request):
    subdata = request.param
    return subdata


# 定义计算类
class TestCacla2():
    # 定义sub方法
    def test_sub(self, get_cacl, get_subdatas):
        result = get_cacl.sub(get_subdatas[0], get_subdatas[1])
        assert get_subdatas[2] == result