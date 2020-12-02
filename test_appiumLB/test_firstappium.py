#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import time

from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction


class TestDW():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'
        # 不停止app，若现在app已经打开了，则不用关掉了再打开
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoardKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 因为之前设置了dontStopAppOnReset
        # self.driver.back()
        self.driver.quit()

    def test_search(self):
        print("搜索测试用例")
        """
        1.打开 雪球app
        2。点击搜索输入框
        3。向搜索输入框里面输入"阿里巴巴"
        4。在搜索结果里面选择"阿里巴巴"，然后进行点击
        5。获取这只上香港 阿里巴巴的股价，并判断 这只股价的价格>200
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]').click()
        current_price = float(self.driver.find_element_by_id('com.xueqiu.android:id/current_price').text)
        assert current_price > 200

    def test_attr(self):
        """
        打开"雪球"应用首页(注意之前的代码是否将雪球页面重置为首页)
        定位首页的搜索框
        判断搜索框是否可用，并查看搜索框name属性值
        打印搜索框这个元素左上角坐标和它的宽高
        想搜索框输入：alibaba
        判断"阿里巴巴"是否可见
        如果可见，打印'搜索成功'点击，如果不可见，打印搜索失败
        :return:
        """
        element_search = self.driver.find_element_by_id('com.xueqiu.android:id/tv_search')
        search_enabled = element_search.is_enabled()
        print(element_search.text)
        # location是定位
        print(element_search.location)
        print(element_search.size)
        if search_enabled == True:
            element_search.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            alibaba_element = self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]')
            # alibaba_element.is_displayed()
            # print(alibaba_element.get_attribute("displayed"))打印为true，说明其内容为true，不是布尔值
            # print(alibaba_element.get_attribute("displayed"))
            ele_displayed = alibaba_element.get_attribute("displayed")
            print(type(ele_displayed))

            if ele_displayed == 'true':
                print("搜索成功")
            else:
                print("搜索失败")

    def test_touchAction(self):
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height*0.8)
        y_end = int(height*0.2)
        action.press(x=x1,y=y_start).wait(200).move_to(x=x1,y=y_end).release().perform()

    def test_get_current(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = self.driver.find_element_by_xpath(
            "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(f"alibaba {current_price}")
        assert float(current_price) > 200

    def test_myinfo(self):

        """
        1.点击我的，进入个人信息页面
        2.点击登录，进入登录页面
        3。输入用户名，输入密码
        4。点击登录
        :return:
        """
        # self.driver.find_element_by_xpath("//*[@resource-id='android:id/tabs']//*[@text='我的']/..").click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码登录")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("12334yf")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("12334")
        self.driver.find_element_by_android_uiautomator('new UiSelector.resourceId("com.xueqiu.android:id/button_next")').click()

    # 滚动查找
    def test_scroll_find_element(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("雪盈证券").instance(0))').click()

        time.sleep(5)

if __name__ == '__main__':
    pytest.main()
