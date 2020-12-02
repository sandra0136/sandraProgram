#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""
    改造1：使用pytest测试框架
"""
def get_datas():
    with open("./datas/addcontacts.yml",encoding='utf-8') as f:
        contact_datas = yaml.safe_load(f)['add']
        print(contact_datas)
        return contact_datas


class TestWeiXin:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        # desired_caps['udid'] = 'emulator-5556'
        # 如果设置了noReset，autoGrantPermissions无效
        desired_caps['autoGrantPermissions'] = True
        # 等待页面空闲的时间。有的页面是动态的(可能一直动态：例如时间)，appium会等待这个页面加载完，这样用例执行就会变慢
        desired_caps['settings[waitForIdleTimeout]'] = 1
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        # 连接超时
        desired_caps['noReset'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        # driver在执行find时都会执行
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_daka(self):
        """
        打卡功能
        :return:
        """
        self.driver.find_element(MobileBy.XPATH,'//*[@text="工作台"]').click()
        # 注意：在屏幕上看不到的元素(可能需要下滑/上滑才能显示在屏幕上)，无法使用定位找到，所以需要滚动查找
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));'
                                 ).click()
        sleep(3)
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/hr_").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'次外出')]").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/auw").click()
        result = self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/oy").text
        assert "外出打卡成功" == result
    # @pytest.mark.parametrize("name,gender,phoneNumber",[
    #     ["mumu","女","13100001111"],
    #     ["Jane","女","13200001111"]
    # ])
    @pytest.mark.parametrize("name,gender,phoneNumber",get_datas())
    def test_addcontact(self,name,gender,phoneNumber):
        """
        添加联系人
        :return:
        """
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        # self.driver.find_element(MobileBy.XPATH,'//*[@text="添加成员"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));'
                                 ).click()

        self.driver.find_element(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        # 注意：不直接使用"必填"，是因为可能表单中存在多个这样的字眼，所以为了找到姓名的输入框，需要通过姓名这个唯一的元素定位到相应的输入框
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"姓名")]/..//*[@text="必填"]').send_keys(name)
        self.driver.find_element(MobileBy.XPATH,'//*[@text="男"]').click()
        gender_ele = WebDriverWait(self.driver,5).until(lambda x:x.find_element(MobileBy.XPATH,'//*[@text="男"]'))
        if gender == "女":
            self.driver.find_element(MobileBy.XPATH,'//*[@text="女"]').click()
        else:
            # self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
            gender_ele.click()
        # 查找手机号：在寻找元素的时候能找到id:com.tencent.wework:id/fow,可以看出这个id,并不具有实际意义，所以建议通过XPATH查找
        # 通过text查找手机元素，但是"手机"不具有唯一性，可以加上手机元素的其他属性一起定位
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"手机") and @class="android.widget.TextView"]/..//*[@class="android.widget.EditText"]').send_keys(phoneNumber)
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"添加成员")]/../../../../..//*[contains(@text,"保存")]').click()
        sleep(2)
        # 检查一下是否有弹框
        print(self.driver.page_source)
        mytoast = self.driver.find_element(MobileBy.XPATH,'//*[@class="android.widget.Toast"]').text
        assert "添加成功" == mytoast

    def test_delember(self):
        """
        删除联系人
        :return:
        """
        # self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="e"]').click()
        # self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/i6d").click()
        # self.driver.find_element(MobileBy.XPATH,'//*[@text="编辑成员"]').click()
        # self.driver.find_element(MobileBy.XPATH,'//*[@text="e"]').click()
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("删除成员").instance(0));'
        #                          ).click()
        # self.driver.find_element(MobileBy.XPATH,'//*[@text="确定"]').click()
        # if self.driver.find_element(MobileBy.XPATH,'//*[@text="e"]').is_displayed() is False:
        #     assert '删除成功'
        """
            删除联系人：通过查找联系人，然后获取结果列表页中的元素个数，判断是否存在需要被删除的联系人，
            有就删除第一个，删除完后之后，再通过查找联系人，获取结果列表中的元素个数，
            最后断言两个元素个数之差是否为1，则判断删除是否成功
        """
        name = "sandy"
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/i6n").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/gpg").send_keys(name)
        eles = self.driver.find_elements(MobileBy.XPATH,f"//*[@text='{name}']")
        if len(eles) < 2:
            print("没有可删除的人")
            return
        eles[1].click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/i6d").click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="编辑成员"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("删除成员").instance(0));'
                                 ).click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="确定"]').click()
        eles_del = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        assert len(eles)-1 == len(eles_del)



