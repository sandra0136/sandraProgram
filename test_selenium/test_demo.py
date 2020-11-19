#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo0():
    def setup_method(self):
        # 复用已有的浏览器。浏览器窗口必须停在测试页面
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        # self.driver = webdriver.Chrome()
        # self.driver.get("https://ceshiren.com/")
        self.driver.maximize_window()
        # 隐式等待，动态的等待元素，最好在实例化driver之后立刻去设置
        self.driver.implicitly_wait(3)

    def teardown_method(self):
        self.driver.quit()

    def test_demo0(self):
        # self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.XPATH,'//*[@id="ember41"]/a').click()
        ele = self.driver.find_element(By.XPATH,'//*[@id="ember158"]/a')
        sleep(3)
        print(ele.get_attribute("class"))
        assert 'active' == ele.get_attribute("class")