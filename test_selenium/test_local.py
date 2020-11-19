#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")

    def test_wait(self):
        # self.driver.find_element(By.ID, 'kw').send_keys("hogwards")
        self.driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("hogwards")
        self.driver.find_element(By.ID,'su').click()