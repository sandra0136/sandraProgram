#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver import ActionChains

from test_file_alter.base import Base


class TestAlter(Base):
    def test_alter(self):
        """
        打开网页https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
        操作窗口右侧页面，将元素1拖拽到元素2
        这时候会有一个alter弹框，点击弹框中的确定
        然后在点击"点击运行"
        关闭网页
        :return:
        """
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame('iframeResult')
        drag = self.driver.find_element_by_id('draggable')
        drop = self.driver.find_element_by_id('droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        sleep(3)
        print("点击 alter 确认")
        self.driver.switch_to.alert.accept()
        # 弹框消失后，点击'点击运行'按钮.此时需要从frame中切换出来。
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id('submitBTN').click()
        sleep(3)