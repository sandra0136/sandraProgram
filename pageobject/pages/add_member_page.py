#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from pageobject.pages.basepage import BasePage
from pageobject.pages.contact_page import ContactPage


class AddMemberPage(BasePage):
    _name = (By.ID, 'username')
    _memberAdd_acctid = (By.ID, 'memberAdd_acctid')
    _memberAdd_phone = (By.ID, 'memberAdd_phone')
    _cancel = (By.CSS_SELECTOR, '[node-type="cancel"]')

    # 保存并填写信息
    def add_member(self, name, acctid, memberAdd_phone):
        self.find(*self._name).send_keys(name)
        self.find(*self._memberAdd_acctid).send_keys(acctid)
        self.find(*self._memberAdd_phone).send_keys(memberAdd_phone)

        # self.driver.find_element(*self._name).send_keys(name)
        # self.driver.find_element_by_id('memberAdd_acctid').send_keys(acctid)
        # self.driver.find_element_by_id('memberAdd_phone').send_keys(memberAdd_phone)
        # 返回自己，是为了返回当前页面时，依然可以使用链式调用
        return self

    # 保存
    def save_member(self):
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        return ContactPage(self.driver)

    # 取消
    def cancel_member(self):
        self.find(By.CSS_SELECTOR, '.js_btn_cancel').click()
        # 不加*，self._cancel为一个元素
        self.wait_for_clickable(self._cancel)
        # self.find(By.CSS_SELECTOR,'[node-type="cancel"]').click()
        self.find(*self._cancel).click()
        return ContactPage(self.driver)
