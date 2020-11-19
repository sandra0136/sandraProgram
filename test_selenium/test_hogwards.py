#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from selenium import webdriver

class TestHogwards():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        pass
    def teardown(self):
        self.driver.quit()
        pass
    def test_hogwards(self):
        self.driver.get("https://testerhome.com")
        self.driver.find_element_by_link_text("社团").click()
        pass
