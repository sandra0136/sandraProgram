#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from test_appium.page.app import App


class TestContact:
    def setup(self):
        """
        应用的启动
        :return:
        """
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        """
        应用关闭
        :return:
        """
        self.app.stop()

    def test_addcontact(self):
        name = "xixi"
        gender = "男"
        phohenum= "13300001111"
        mypage = self.main.goto_addresslist().add_member().addcontact_menual().edit_name(name). \
            edit_gender(gender).edit_phonenum(phohenum).click_save()
        mytoast = mypage.get_toast()
        assert "添加成功" == mytoast
