#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from pageobject.pages.add_member_page import AddMemberPage
from pageobject.pages.basepage import BasePage
from pageobject.pages.contact_page import ContactPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    _add_member = (By.CSS_SELECTOR, '[node-type="addmember"]')
    _menu_contacts = (By.ID, 'menu_contacts')

    # 点击"通讯录"-跳转到通讯录页面
    def go_to_contact(self):
        # 对ContactPage类的实例化，表示业务逻辑的转换关系
        self.find(*self._menu_contacts).click()
        return ContactPage(self.driver)

    # 点击"添加成员"-跳转到添加成员页面
    def go_to_add_memeber(self):
        self.find(*self._add_member).click()
        return AddMemberPage(self.driver)


if __name__ == '__main__':
    main = MainPage()
    main.go_to_add_memeber().add_member().save_member()
