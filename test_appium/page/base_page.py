#!/usr/local/bin python3
# -*- coding: utf-8 -*-
"""
BasePage:做为基类
最基本的方法：初始化driver，find，显示等待，...
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        self.find(locator).click()

    def find_and_sendkeys(self, locator, value):
        self.find(locator).send_keys(value)

    def find_by_scroll_and_click(self, text):
        ele = (MobileBy.ANDROID_UIAUTOMATOR,
               'new UiScrollable(new UiSelector()'
               '.scrollable(true).instance(0))'
               '.scrollIntoView(new UiSelector()'
               f'.text("{text}").instance(0));'
               )
        self.find_and_click(ele)

    def find_and_get_text(self,locator):
        return self.find(locator).text

    def get_toastText(self):
        ele = (MobileBy.XPATH, '//*[@class="android.widget.Toast"]')
        mytoast = self.find_and_get_text(ele)
        return mytoast

    def wait(self,locator):
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*locator))