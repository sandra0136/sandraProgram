#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from selenium import webdriver
class TestFirefox:
    def test_fire(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.baidu.com")