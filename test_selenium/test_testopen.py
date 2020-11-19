#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestOpen():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardowm_method(self, method):
        self.driver.quit()

    def test_testopen(self):
        self.driver.get("https://home.testing-studio.com/")
        time.sleep(2)
        self.driver.set_window_size(1478, 825)
        time.sleep(2)
        self.driver.close()
