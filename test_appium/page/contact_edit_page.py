#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.page.base_page import BasePage
from test_appium.page.member_invite_page import MemberInvitePage

"""
成员编辑页
"""
class ContactEditPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    name_element = (MobileBy.XPATH,'//*[contains(@text,"姓名")]/..//*[@text="必填"]')
    gender_element = (MobileBy.XPATH, '//*[@text="男"]')
    female_element = (MobileBy.XPATH, '//*[@text="女"]')
    phonenum_element = (MobileBy.XPATH,'//*[contains(@text,"手机") and @class="android.widget.TextView"]/..//*[@class="android.widget.EditText"]')
    save_element = (MobileBy.XPATH,'//*[contains(@text,"添加成员")]/../../../../..//*[contains(@text,"保存")]')
    def edit_name(self,name):
        self.find_and_sendkeys(self.name_element,name)
        return self

    def edit_gender(self,gender):
        self.find_and_click(self.gender_element)
        self.wait(self.gender_element)
        if gender == '女':
            self.find_and_click(self.female_element)
        else:
            self.find_and_click(self.gender_element)

        # self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
        # gender_ele = WebDriverWait(self.driver, 5).until(lambda x: x.find_element((MobileBy.XPATH, '//*[@text="男"]'))
        # if gender == "女":
        #     self.driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()
        # else:
        #     # self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
        #     gender_ele.click()
        return self

    def edit_phonenum(self,phoneNumber):
        # self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"手机") and @class="android.widget.TextView"]/..//*[@class="android.widget.EditText"]')\
        #     .send_keys(phoneNumber)
        self.find_and_sendkeys(self.phonenum_element,phoneNumber)
        return self

    def click_save(self):
        # self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"添加成员")]/../../../../..//*[contains(@text,"保存")]').click()
        self.find_and_click(self.save_element)
        return MemberInvitePage(self.driver)