#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        ele_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        ele_doubleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        ele_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(ele_click)
        action.context_click(ele_rightclick)
        action.double_click(ele_doubleclick)
        sleep(3)
        action.perform()
        sleep(5)

    # 将光标移动到某个元素
    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("http://www.baidu.com")
        # sleep(5)
        # WebDriverWait(self.driver,5).until(self.driver.find_element(By.XPATH,'//*[@id="s-usersetting-top"]').is_displayed())
        # ele = self.driver.find_element(By.XPATH,'//*[@id="s-usersetting-top"]')
        ele = self.driver.find_element_by_link_text("贴吧")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(5)

    # 拖拽
    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_ele = self.driver.find_element_by_id("dragger")
        drop_ele = self.driver.find_element_by_xpath("/html/body/div[2]")
        # print(f"drap_ele:{type(drag_ele)}")
        # print(f"drop_ele:{type(drop_ele)}")
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_ele, drop_ele).perform()
        action.click_and_hold(drag_ele).release(drop_ele).perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)

# if __name__ == '__main__':
#     pytest.main(['-v','-s','test_ActionChains.py'])
