#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import shelve

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

from selenium.webdriver.common.by import By


class TestCookie:


    def setup_method(self):
        # 复用已有的浏览器。条件：只有一个浏览器被打开，且通过命令行打开；浏览器活动窗口必须停在测试页面
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        # self.driver = webdriver.Chrome()
        # 隐式等待，动态的等待元素，最好在实例化driver之后立刻去设置
        self.driver.implicitly_wait(3)


    def teardown_method(self):
        self.driver.quit()


    def test_cookie(self):
        # get_cookies获取当前页面的cookies
        cookies = self.driver.get_cookies()
        print(cookies)
        # 打开index目录，此时需要登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 带有登录信息的cookie,cookie具有时效性
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851343080665'},{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851343080665'},{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'},{'domain': '.qq.com', 'expiry': 1602765832.23023, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.2038435128.1602666777'},{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'XItPtrzwtaAWRLEF6SHVRbqcBh7S8cWOip1aB4et0Lp3cBEQU5vqZuydLHshO0p3'},{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a9608287'},{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1602679401'},{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '02600333'},{'domain': 'work.weixin.qq.com', 'expiry': 1602698276, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '9cj4kq'},{'domain': '.qq.com', 'expiry': 1665751432, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1240428279.1600928230'},{'domain': '.work.weixin.qq.com', 'expiry': 1605271435, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'},{'domain': '.qq.com', 'expiry': 1602679474, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'},{'domain': '.qq.com', 'expiry': 1603627511, 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': False, 'value': 'o3420974921'},{'domain': '.qq.com', 'expiry': 1897538930, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '2c403cdd79a6cc34'},{'domain': '.work.weixin.qq.com', 'expiry': 1632399798, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'},{'domain': '.qq.com', 'expiry': 1628328207, 'httpOnly': False, 'name': 'sd_cookie_crttime', 'path': '/', 'secure': False, 'value': '1596792207151'},{'domain': '.qq.com', 'expiry': 1628328207, 'httpOnly': False, 'name': 'sd_userid', 'path': '/', 'secure': False, 'value': '28531596792207151'},{'domain': '.qq.com', 'expiry': 1898954638, 'httpOnly': False, 'name': 'XWINDEXGREY', 'path': '/', 'secure': False, 'value': '0'},{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'K027i2HjrSzsFCmga293zC5OBu1ZtbIK5vbex-O9PtxzOhv9ByP77LIrszMJWvYfBiW5qfUvzVY0GklsqWFm3hYoNLgsivTg7jWVeZxidUHTzLfMyrIvkNQ6R9p6io45MkgHcyFML94K-If85XEDiY7d7KBg5Xzb0j1xNf1Otyc9oNzp2sCPNfZ0jcJsN94TZghW7DvkdynTLlvbqqANI6egXswfeeJRkCxQWTLIUKMAXY8BDGS8UkHaNvdPpBy_5U98AP6JyLb2lkAUE8GaEA'},{'domain': '.work.weixin.qq.com', 'expiry': 1634215401, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1600928228,1602666774,1602673394,1602679401'},{'domain': '.qq.com', 'expiry': 1875462528, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '1_291553943'},{'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '59b2f291560c4b0fd3777950e40a3278a190cd5f0099f7369201a254fd03e7c7'},{'domain': '.qq.com', 'expiry': 1603627511, 'httpOnly': False, 'name': 'lskey', 'path': '/', 'secure': False, 'value': '00010000709a6193e984ba71343e2236802f6e8f84938afb7e453cf01a96880c16c450a18e465219895489fd'},{'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'm0aMRhUln2'},{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'},{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324967163109'},{'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '23882435'},{'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '3695585280'}]
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                # cookie不支持浮点数
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        # 重新打开 带有cookie信息的 index页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(2)').click()
        self.driver.find_element(By.CSS_SELECTOR,'.ww_fileImporter_fileContainer_uploadInputMask').send_keys("/Users/sandra/Desktop/工作簿4.xlsx")
        assert '工作簿4.xlsx' == self.driver.find_element(By.CSS_SELECTOR,'.ww_fileImporter_fileContainer_fileNames').text
        sleep(3)
    # 实现cookie数据的持久化存储
    @pytest.mark.skip
    def test_shelve(self):
        # shelve是python内置的模块，相当于小型数据库
        # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851343080665'},{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851343080665'},{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'},{'domain': '.qq.com', 'expiry': 1602765832.23023, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.2038435128.1602666777'},{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'XItPtrzwtaAWRLEF6SHVRbqcBh7S8cWOip1aB4et0Lp3cBEQU5vqZuydLHshO0p3'},{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a9608287'},{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1602679401'},{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '02600333'},{'domain': 'work.weixin.qq.com', 'expiry': 1602698276, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '9cj4kq'},{'domain': '.qq.com', 'expiry': 1665751432, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1240428279.1600928230'},{'domain': '.work.weixin.qq.com', 'expiry': 1605271435, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'},{'domain': '.qq.com', 'expiry': 1602679474, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'},{'domain': '.qq.com', 'expiry': 1603627511, 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': False, 'value': 'o3420974921'},{'domain': '.qq.com', 'expiry': 1897538930, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '2c403cdd79a6cc34'},{'domain': '.work.weixin.qq.com', 'expiry': 1632399798, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'},{'domain': '.qq.com', 'expiry': 1628328207, 'httpOnly': False, 'name': 'sd_cookie_crttime', 'path': '/', 'secure': False, 'value': '1596792207151'},{'domain': '.qq.com', 'expiry': 1628328207, 'httpOnly': False, 'name': 'sd_userid', 'path': '/', 'secure': False, 'value': '28531596792207151'},{'domain': '.qq.com', 'expiry': 1898954638, 'httpOnly': False, 'name': 'XWINDEXGREY', 'path': '/', 'secure': False, 'value': '0'},{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'K027i2HjrSzsFCmga293zC5OBu1ZtbIK5vbex-O9PtxzOhv9ByP77LIrszMJWvYfBiW5qfUvzVY0GklsqWFm3hYoNLgsivTg7jWVeZxidUHTzLfMyrIvkNQ6R9p6io45MkgHcyFML94K-If85XEDiY7d7KBg5Xzb0j1xNf1Otyc9oNzp2sCPNfZ0jcJsN94TZghW7DvkdynTLlvbqqANI6egXswfeeJRkCxQWTLIUKMAXY8BDGS8UkHaNvdPpBy_5U98AP6JyLb2lkAUE8GaEA'},{'domain': '.work.weixin.qq.com', 'expiry': 1634215401, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1600928228,1602666774,1602673394,1602679401'},{'domain': '.qq.com', 'expiry': 1875462528, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '1_291553943'},{'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '59b2f291560c4b0fd3777950e40a3278a190cd5f0099f7369201a254fd03e7c7'},{'domain': '.qq.com', 'expiry': 1603627511, 'httpOnly': False, 'name': 'lskey', 'path': '/', 'secure': False, 'value': '00010000709a6193e984ba71343e2236802f6e8f84938afb7e453cf01a96880c16c450a18e465219895489fd'},{'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'm0aMRhUln2'},{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'},{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324967163109'},{'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '23882435'},{'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '3695585280'}]
        # db = shelve.open('./mydb/cookies')
        # 将数据写入到数据库中
        # db['cookie'] = cookies
        # db.close()
        # 将数据读出来
        db = shelve.open('./mydb/cookies')
        cookies = db['cookie']
        print(cookies)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)

