#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        # 所有find都会触发隐式等待
        self.driver.implicitly_wait(3)

    def test_wait(self):
        # 点击所有分类
        self.driver.find_element(By.XPATH, '//*[@id="ember39"]').click()

        def wait(x):
            # 点击所有分类后，看最新有没有出现
            return len(self.driver.find_elements(By.XPATH, '//*[@class="table-heading"]')) >= 1

        WebDriverWait(self.driver, 10).until(wait)
        # 有最新出现，则点击热门；不然超时报错
        self.driver.find_element(By.XPATH, '//*[@id="ember146"]').click()
