#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from pageobject.pages.basepage import BasePage



class ContactPage(BasePage):
    # find_element找到两个会拿第一个
    _add_member = (By.CSS_SELECTOR, '.ww_operationBar .js_add_member')
    _cancel = (By.CSS_SELECTOR, '.js_btn_cancel')

    # 点击"添加成员"-跳转到添加成员页面
    def go_to_add_member(self):
        # 解决循环导入问题
        from pageobject.pages.add_member_page import AddMemberPage
        # todo:完成点击添加成员操作
        # 确认添加成员按钮是可点的
        self.wait_for_clickable(self._add_member)
        while True:
            self.find(*self._add_member).click()
            # 报错被捕获，执行except 循环点击找元素操作，直到找到为止
            try:
                # 找到添加成员页面的某个元素
                res = self.find(*self._cancel)
                # 如果存在的话就跳出循环，如果不存在的话，就报错
                if res is not None:
                    break
            except:
                print("暂时没找到")
        return AddMemberPage(self.driver)

    # 断言需要的信息
    def get_member_list(self):
        eles = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        return [name.text for name in eles]

    # 添加部门
    def add_department_click(self):
        from pageobject.pages.departmen_page import DepartmantPage
        self.find(By.CSS_SELECTOR,'.js_create_dropdown').click()
        self.find(By.CSS_SELECTOR,'.js_create_party').click()
        return DepartmantPage(self.driver)
