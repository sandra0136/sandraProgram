#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from selenium import webdriver


class TestData:
    def test_data(self):
        driver = webdriver.Chrome()
        driver.get("https://home.testing-studio.com")
        driver.execute_script("return JSON.stringify(window.performance.timing)")