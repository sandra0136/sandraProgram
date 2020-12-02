#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from appium import webdriver
from hamcrest import *


class TestGetAttr:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        # 每次都可以进入首页
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'
        # 在上一个操作执行完成后，不要把app进行重置
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoardKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 因为之前设置了dontStopAppOnReset
        # self.driver.back()
        self.driver.quit()

    def test_get_attr(self):
        search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        # 可以获取哪些属性，可以通过源码中的units的attribute类查看
        print(search_ele.get_attribute("content-desc"))
        print(search_ele.get_attribute("resource-id"))
        print(search_ele.get_attribute("enabled"))
        print(search_ele.get_attribute("clickable"))

    def test_hamrest(self):
        assert_that(10,equal_to(10),"错误信息")
        assert_that(8,close_to(10,2))
