#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestInteration:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        # mumu上面不可模拟电话，所以这里使用的emulator
        desired_caps['deviceName'] = 'emulator-5556'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        # desired_caps['noReset'] = 'true'
        # # 在上一个操作执行完成后，不要把app进行重置
        # desired_caps['dontStopAppOnReset'] = 'true'
        # desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoardKeyBoard'] = 'true'
        # 模拟器的控制,只能使用sdk自带的emulator
        desired_caps['avd'] = 'A6'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub")
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_mobile(self):
        self.driver.make_gsm_call('13829731939',GsmCallActions.CALL)

        self.driver.send_sms('13829731839',"hi")
        # 模拟网络：数据，Wi-Fi，飞行
        self.driver.set_network_connection(1)
        # 保存截图
        self.driver.get_screenshot_as_file('./img.png')
        # 录屏(8.0,要考虑系统版本和手机型号)
        self.driver.stop_recording_screen()