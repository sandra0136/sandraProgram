#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from time import sleep

from test_selenium.base import Base
class TestWindows(Base):
    def test_window(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_xpath('//*[@id="u1"]/a').click()
        self.driver.find_element_by_link_text("立即注册").click()
        print("第一个窗口："+self.driver.current_window_handle)
        print("点击注册后，所有的窗口："+self.driver.window_handles[0]+","+self.driver.window_handles[1])
        # 点击立即注册后，会打开新的页面，driver还在第一个窗口中，没有切换
        windows = self.driver.window_handles
        print(f"11:{type(self.driver.window_handles)}")
        # 切换到注册窗口
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("hogwards")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("138293932323")
        # 返回到百度首页
        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("291553943@qq.com")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("0136sy")
        sleep(3)
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(3)

