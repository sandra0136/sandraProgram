#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *


class TestParam:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        # 不清除缓存
        desired_caps['noReset'] = 'true'
        # 在上一个操作执行完成后，不要把app进行重置
        desired_caps['dontStopAppOnReset'] = 'true'
        # 跳过一些安装
        desired_caps['skipDeviceInitialization'] = 'true'
        # 中文输入
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoardKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 因为之前设置了dontStopAppOnReset
        # self.driver.back()
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/action_close").click()
    @pytest.mark.parametrize('searchkey,type,price',[
        ('alibaba','BABA',280),
        ('xiaomi','01810',25)
    ])
    def test_search(self,searchkey,type,price):
        """
        1.打开雪球应用
        2。点击搜索框
        3。输入 搜索词"alibaba" or "xiaomi"
        4.点击第一个搜索结果
        5。判断 股票价格
        :return:
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/name").click()
        current_price_ele = self.driver.find_element(MobileBy.XPATH,f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        current_price = current_price_ele.text
        print(current_price)
        assert_that(current_price,close_to(price,price*0.1))


