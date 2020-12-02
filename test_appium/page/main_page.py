#!/usr/local/bin python3
# -*- coding: utf-8 -*-
"""
主页：通过adb shell dumpsys window|grep mCurrentFocus可以获取页面的名称。
如何定义一个页面：
    方法1：通过上面的adb命令获取的页面名称相同，则为一个页面
    方法2：视觉上的一个页面（可能通过上面adb获取的页面名称一样）

"""
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.addresslist_page import AddressListPage
from test_appium.page.base_page import BasePage
from test_appium.page.workbench_page import WorkBenchPage


class MainPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    addresslist_element = (MobileBy.XPATH, '//*[@text="通讯录"]')
    def goto_addresslist(self):
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.find_and_click(self.addresslist_element)
        return AddressListPage(self.driver)

    def goto_workbench(self):
        return WorkBenchPage()
