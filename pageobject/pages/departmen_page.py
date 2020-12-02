#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from pageobject.pages.basepage import BasePage
from pageobject.pages.contact_page import ContactPage


class DepartmantPage(BasePage):
    _departnameInput = (By.CSS_SELECTOR,'[name="name"]')
    _selectdepart = (By.CSS_SELECTOR,'.js_toggle_party_list')
    _select_owned_depart = (By.XPATH,'//a[@id="1688851343080666_anchor"]')
    _save = (By.CSS_SELECTOR, '#__dialog__MNDialog__ [d_ck="submit"]')
    _cancel = (By.CSS_SELECTOR,'#__dialog__MNDialog__ [d_ck="cancel"]')

    def add_department(self,dep_name):
        self.find(*self._departnameInput).send_keys(dep_name)
        self.find(*self._selectdepart).click()
        eles = self.finds(*self._select_owned_depart)
        if len(eles) == 2:
            eles[1].click()
        return self

    def save_department(self):
        self.find(*self._save).click()
        return ContactPage(self.driver)

    def cancel_department(self):
        self.find(*self._cancel).click()
        return ContactPage(self.driver)