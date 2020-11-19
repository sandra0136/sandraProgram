#!/usr/local/bin python3
# -*- coding: utf-8 -*-
"""
添加成员页面
"""
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.base_page import BasePage


class MemberInvitePage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    addmember_element = (MobileBy.XPATH,'//*[@text="手动输入添加"]')
    def addcontact_menual(self):
        from test_appium.page.contact_edit_page import ContactEditPage
        # self.driver.find_element(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        self.find_and_click(self.addmember_element)
        return ContactEditPage(self.driver)
    # 对于某一步骤操作完成后，一般会弹出toast。这样可以用它作为断言。
    # toast在哪个页面出现，就定义在哪个页面.(这样容易维护)
    def get_toast(self):
        mytoast = self.get_toastText()
        return mytoast