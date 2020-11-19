#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from test_selenium.base import Base
class TestFrame(Base):
    print("ddd")
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        # self.driver.switch_to_frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)
        # self.driver.switch_to.parent_frame()
        self.driver.switch_to_default_content()
        print(self.driver.find_element_by_id("submitBTN").text)