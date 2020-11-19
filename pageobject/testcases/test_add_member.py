#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.webkitgtk.options import Options

from pageobject.pages.add_member_page import AddMemberPage
from pageobject.pages.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        self.main = MainPage()

    # 测试用例：添加成员1：1.从首页点击"添加成员"，跳转到添加成员页面；2.添加成员并保存
    def test_add_member(self):
        # 1.打开首页
        # self.main = MainPage()
        # 从首页中点击"添加成员"，跳转到添加成员页面，填写信息后保存。
        namelist = self.main.go_to_add_memeber().add_member("e", "33", 13992338323).save_member().get_member_list()
        assert "e" in namelist

    def test_add_member_fail(self):
        namelist = self.main.go_to_add_memeber().add_member("e1","33", 13992338323).cancel_member().get_member_list()
        print(namelist)
        assert 'e1' not in namelist

    # 测试用例：添加成员2：从首页点击通讯录，跳转到通讯录页面，点击添加成员，填写信息并保存

    def test_contact_member(self):
        # 1.打开首页
        # self.main = MainPage()
        # 2.从首页点击"通讯录"，跳转到通讯录页面；3.点击添加成员，填写信息并保存
        self.main.go_to_contact().go_to_add_member().add_member("a","3", 18992338323)

    def test_add_department(self):
        self.main.go_to_contact().add_department_click().add_department("测试").save_department()

    def teardown(self):
        self.main.driver.quit()

    @pytest.mark.skip
    def test_add(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851343080665'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851343080665'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 1603114053, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1755785653.1603025077'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'XItPtrzwtaAWRLEF6SHVRYb3Bwgg6-SmXaiaMp_cqX2Zh9wSJWDrn67zpqYRwvrk'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a6052383'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1603027641'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '01639748'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1603056610, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '57lb3l5'},
            {'domain': '.qq.com', 'expiry': 1666099653, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1240428279.1600928230'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1605619666, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 1603027703, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 1603627511, 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': False,
             'value': 'o3420974921'},
            {'domain': '.qq.com', 'expiry': 1897538930, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
             'secure': False, 'value': '2c403cdd79a6cc34'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1632399798, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 1628328207, 'httpOnly': False, 'name': 'sd_cookie_crttime', 'path': '/',
             'secure': False, 'value': '1596792207151'},
            {'domain': '.qq.com', 'expiry': 1628328207, 'httpOnly': False, 'name': 'sd_userid', 'path': '/',
             'secure': False, 'value': '28531596792207151'},
            {'domain': '.qq.com', 'expiry': 1898954638, 'httpOnly': False, 'name': 'XWINDEXGREY', 'path': '/',
             'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': '3FSqQF8HNFyNLhaEYZHneUCRRFqZ16WHBXz22y6d0SIpVTOvPCNPogxwdmZlQYsO5TMQ7OV53RZT4EvEasRQAIKAGIdYWNl40PE-12rfdN12-ZeVa9ckO5MZJ0PdRFl6eFZIOE2mmzJeCcSEuAmF2MGrg2tpj5wWSsbduIKDN61zgYTDFEUPEnZGJdmMhi4hWNhqEgBGb4LnJruEazTWwmrj7aOMi7fHF1jOAcBWmcPyGGPf-A0LF_TDCJ9qTeqr6HQ8xhFvsa-cFJg2AWtWXQ'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1634563641, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
             'value': '1602666774,1602673394,1602679401,1603027641'},
            {'domain': '.qq.com', 'expiry': 1875462528, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
             'secure': False, 'value': '1_291553943'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '59b2f291560c4b0fd3777950e40a3278a190cd5f0099f7369201a254fd03e7c7'},
            {'domain': '.qq.com', 'expiry': 1603627511, 'httpOnly': False, 'name': 'lskey', 'path': '/',
             'secure': False,
             'value': '00010000709a6193e984ba71343e2236802f6e8f84938afb7e453cf01a96880c16c450a18e465219895489fd'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'm0aMRhUln2'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324967163109'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '23882435'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '3695585280'}]
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                # cookie不支持浮点数
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[3]/div[1]/a[1]').click()
        self.driver.find_element_by_id("username").send_keys("hi")
