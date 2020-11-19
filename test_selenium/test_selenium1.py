#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import selenium
from selenium import webdriver

# 注意chromedriver和chrome的版本一致。通过Chrome的帮助查看版本号，然后https://npm.taobao.org/mirrors/chromedriver/下载相应版本的Chromedriver
# 并将其移动到/usr/local/bin下。

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
