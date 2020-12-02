#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TextWXMicro:
    def setup(self):
        caps = {}
        caps['platformName'] = 'android'
        caps['deviceName'] = 'emulator-5554'
        caps['appPackage'] = 'com.tencent.mm.ui.LauncherUI'
        caps['noReset'] = True
        caps['unicodeKeyboard'] = True
        caps['resetKeyboard'] = True
        caps['chromedriverExecutable'] = '/Users/sandra/Documents/mychromedriver/all'
        # 小程序的进程
        # options = ChromeOptions()
        # options.add_experimental_option('androidProcess','com.tencent.mm:appbrand0')
        caps['chromeOptions'] = {
            'androidProcess': 'com.tencent.mm:appbrand0'
        }

        caps['adbPort'] = 5038

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)

        self.driver.find_element(By.XPATH, '//*[@text="通讯录"]')
        self.driver.implicitly_wait(10)

    def test_search(self):
        # 原生自动化测试
        size = self.driver.get_window_size()
        # 滑动
        self.driver.swipe(size['width'] * 0.5, size['height'] * 0.4, size['width'] * 0.5, size['height'] * 0.4)
        # 点击编辑框
        self.driver.find_element(By.CLASS_NAME, "android.widget.EditText").click()
        self.driver.find_element(By.XPATH, "//*[@text='取消']")
        self.driver.find_element(By.CLASS_NAME,"android.widget.EditText").send_keys("雪球")
        self.driver.find_element(By.CLASS_NAME,"android.widget.Button")
        self.driver.find_element(By.CLASS_NAME,'android.widget.Button').click()
        self.driver.find_element(By.XPATH,"//*[@text='自选']")

        print(self.driver.contexts)
        # 进入webview
        self.driver.switch_to.context('WEBVIEW_xweb')
        self.driver.implicitly_wait(10)
        self.find_top_window()

        # css定位
        self.driver.find_element(By.CSS_SELECTOR,'[src*=stock_add]').click()
        # 等待新窗口
        WebDriverWait(self.driver,30).until(lambda x: len(self.driver.window_handles) > 2)
        self.find_top_window()
        self.driver.find_element(By.CSS_SELECTOR,'._input').click()
        # 输入
        self.driver.switch_to.context("NATIVE_APP")
        ActionChains(self.driver).send_keys("alibaba").perform()
        # 点击
        self.driver.switch_to.context("WEBVIEW_APP")
        self.driver.find_element(By.CSS_SELECTOR,".stock_item")
        self.driver.find_element(By.CSS_SELECTOR, ".stock_item").click()


    def find_top_window(self,driver=None):
        for window in self.driver.window_handles:
            print(window)
            if ":VISIBLE" in self.driver.title:
                print(self.driver.title)
                return True
            else:
                self.driver.switch_to.window(window)
        return False
