#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWebViewapi:
    def setup(self):
        desi_caps = {
            'platformName':'android',
            'appPackage':'io.appium.android.apis.ApiDemos',
            'deviceName':'emulator-5554',
            # 把多个版本的driver放在一个文件夹下面
            'chromedriverExecutableDir':'/Users/sandra/Documents/mychromedriver/all',
            'chromedriverChromeMappingFile':'/Users/sandra/sandraProgram/appium_webview/mapping.json'
            # 'chromedriverExecutable':'/Users/sandra/Downloads/chromedriver'

        }
        self.driver = webdriver.Remote("http://127.0.0.1:4732/wd/hub",desi_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_webview(self):
        self.driver.find_element_by_accessibility_id('Views').click()
        # 此处为原生页面
        print(self.driver.context)
        webview = "WebView"
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0).'
                                                        f'scrollIntoView(new UiSelector().text(f"{webview}"))')
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'i has no focus').send_keys("this is a test")
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'i am a link').click()
        # print(self.driver.page_source)
        # 此处增加webview页面
        print(self.driver.context)
        self.driver._switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(MobileBy.ID,'i_am_a_textbox').send_keys("this is a test")
        self.driver.find_element(MobileBy,'i am a link').click()
        print(self.driver.page_source)