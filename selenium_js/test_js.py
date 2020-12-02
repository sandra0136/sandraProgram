#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from time import sleep

from selenium_js.base import Base
import pytest


class TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        sleep(3)
        ele_search = self.driver.execute_script('return document.getElementById("su")')
        ele_search.click()
        sleep(3)
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        sleep(3)
        for code in [
            'return document.title','return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))
        self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)")

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script('date_ele=document.getElementById("train_date");date_ele.removeAttribute("readonly")')
        self.driver.execute_script('document.getElementById("train_date").value="2022-1-1"')
        sleep(3)
        print(self.driver.execute_script('return document.getElementById("train_date").value'))