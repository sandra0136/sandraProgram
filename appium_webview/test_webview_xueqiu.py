#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebView:
    def setup(self):
        desc_caps = {
            'platformName': 'android',
            'platformVersion': '6.0',
            'appPackage': 'com.xueqiu.android',
            'appActivity': 'com.xueqiu.android/com.xueqiu.android.common.MainActivity',
            'deviceName': 'emulator-5554',
            'noRest':True,
            'skipServerInstallation':'true',
            # 注意一定要添加引擎路径。
            'chromedriverExecutable': '/Users/sandra/Downloads/chromedriver'
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desc_caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()

    def test_webview(self):
        # 点击交易
        self.driver.find_element(MobileBy.XPATH,"//*[@text='交易']").click()
        A_locator = (MobileBy.XPATH,"//*[@id='Layout_app_3v4'/div/div/ul/li[1]/div[2]/h1")
        # self.driver.find_element(MobileBy.XPATH,"//*[@id='Layout_app_3v4'/div/div/ul/li[1]/div[2]/h1").click()
        # 有可能driver.contexts里面是乱序的，则遍历寻找
        # 切换上下文（因为原生应用和webview需要切换）
        self.driver._switch_to.context(self.driver.contexts[-1])
        print(self.driver.window_handles)
        # 点击"A股开户"
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(A_locator))
        self.driver.find_element(*A_locator).click()
        # 点击前后打印一下所有的窗口
        print(self.driver.window_handles)
        # 切换窗口
        self.driver.switch_to.window()
        # 显示等待
        phonenumber_locator = (MobileBy.ID,'phone-number')
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(phonenumber_locator))
        # 输入用户名和验证码，点击开户
        self.driver.find_element(*phonenumber_locator).send_keys("135353546434")
        self.driver.find_element(MobileBy.ID,'code').send_keys('1234')
        self.driver.find_element(MobileBy.XPATH,'/html/body/div/div/div[2]/div/div[2]/h1').click()
