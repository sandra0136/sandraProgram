#!/usr/local/bin python3
# -*- coding: utf-8 -*-
"""
  app.py:存放一些特有的操作
  比如：启动应用，关闭应用，重启应用，进入到首页
"""
from appium import webdriver

from test_appium.page.base_page import BasePage
from test_appium.page.main_page import MainPage


class App(BasePage):
    # 启动App
    def start(self):
        if self.driver == None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = 'emulator-5554'
            # desired_caps['udid'] = 'emulator-5556'
            # 如果设置了noReset，autoGrantPermissions无效
            desired_caps['autoGrantPermissions'] = True
            # 等待页面空闲的时间。有的页面是动态的(可能一直动态：例如时间)，appium会等待这个页面加载完，这样用例执行就会变慢
            desired_caps['settings[waitForIdleTimeout]'] = 1
            desired_caps['appPackage'] = 'com.tencent.wework'
            desired_caps['appActivity'] = '.launch.WwMainActivity'
            # 连接超时
            desired_caps['noReset'] = 'true'
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            # driver在执行find时都会执行
            self.driver.implicitly_wait(5)
        else:
            # lauch_app():启动desired_caps中设置的的appActivity，起到复用的效果
            # self.driver.start_activity(appPackage,appActivity):可以启动任何app的页面
            self.driver.launch_app()
        return self

    # 重启
    def restart(self):
        self.driver.close()
        self.driver.launch_app()

    # 停止
    def stop(self):
        self.driver.quit()

    # 进入首页
    def goto_main(self) -> MainPage:
        """
        跳转到首页
        :return:
        """
        return MainPage(self.driver)
