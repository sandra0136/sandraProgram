#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestToast:
    def setup(self):
        desire = {
            'platformName':'android',
            'platformVersion':'6.0',
            'deviceName':'emulator-5554',
            'appPackage':'io.appium.android.apis',
            'appActivity':'io.appium.apis.view.PopupMenu1',
            'automationName':'uiautomator2'
        }
        self.driver = webdriver.Remote("http://127.0.0.0:4723/wd/hub",desire)
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_toast(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"Make A POPUP").click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="search"]').click()
        print(self.driver.page_source)
        # print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text)
        print(self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"Clicked popup")]').text)