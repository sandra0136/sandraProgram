#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator_5554'
        desired_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
        desired_caps['appActivity'] = 'com.samsung.ui.MainActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()
    def test_touchaction(self):
        action = TouchAction(self.driver)
        # self.driver.find_element_by_id("")
        action = TouchAction(self.driver)

        action.press(x=200,y=395).move_to(x=210,y=395).move_to(x=250,y=395).move_to(x=250,y=410)\
            .move_to(x=250,y=450).release().perform()
