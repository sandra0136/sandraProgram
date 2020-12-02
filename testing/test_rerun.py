#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from time import sleep

import pytest


def test_rerun1():
    sleep(0.3)
    assert 2 == 2


# pytest_rerunfailures会对失败的用例执行rerun操作。

@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_rerun2(connectDB):
    connectDB
    print("连接完毕")
    sleep(0.5)
    assert 1 == 2


def test_rerun3():
    sleep(0.5)
    assert 3 == 2
