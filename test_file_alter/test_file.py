#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from test_file_alter.base import Base
from time import sleep


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_id("stfile").send_keys("/Users/sandra/sandraProgram/pythoncode/1.png")
        sleep(3)