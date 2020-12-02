#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


class TestForm:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("123")
        self.driver.find_element_by_id("user_password").send_keys("password")
        self.driver.find_element_by_id("user_remember_me").click()
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input')
        sleep(3)
    def test_form_login(self):
        # 打开登录页面
        self.driver.get("https://testerhome.com/account/sign_in")
        # 定位输入用户名的输入框
        user_id = self.driver.find_element_by_id("user_login")
        # 输入用户名"123"
        user_id.send_keys("123")
        # 获取输入框的内容
        print(user_id.get_attribute("value"))
        # 输入密码
        passwd = self.driver.find_element(By.ID,"user_password")
        passwd.send_keys("456")
        # 获取输入框的内容
        print(passwd.get_attribute("value"))
        self.driver.find_element(By.CSS_SELECTOR,"#user_remember_me").click()
        self.driver.find_element(By.NAME,"commit").click()
        sleep(10)