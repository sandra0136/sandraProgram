#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import requests


# 创建部门成功->更新部门成功->删除部门
class TestDepartment:
    # 不要频繁访问gettoken接口
    def setup_class(self):
        corpid = "ww2dfe2dadeb083b38"
        corpsecret = 'VD9eqBN3cKwNA-fiJVwDigA1nE-dHes73gVWQUW_rnY'
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        # 定义请求参数
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        # 发get请求
        r = requests.get(url, params=params)
        # 获取token
        self.token = r.json()['access_token']

    def test_create_department(self):
        """
        创建部门
        :return:
        """
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create'
        # 定义请求参数
        param = {
            "access_token": self.token,
        }
        # 定义请求体
        data = {
            "name": "我好",
            "name_en": "wohao",
            "parentid": 1,
            "order": 1,
            "id": 2
        }
        # 发post请求。json=data,这里使用json是因为接口在定义请求体时，要求使用json。
        r = requests.post(url, json=data, params=param)
        print(r.json())
        get_deparment_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url= get_deparment_list_url)
        assert list.json()["department"][1]['name'] == "我好"
        assert r.json()["errcode"] == 0 and r.json()["errmsg"] == 'created'

    def test_update_department(self):
        data = {
               "id": 2,
               "name": "深圳研发",
               "name_en": "RDGZ",
               "parentid": 1,
               "order": 1
            }
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        r = requests.post(url= update_url,json = data)
        get_deparment_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url=get_deparment_list_url)
        assert list.json()["department"][1]['name'] == data['name']
        assert r.json()["errcode"] == 0 and r.json()["errmsg"] == 'updated'
    def test_delete_department(self):
        delete_url = f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={2}'
        requests.get(delete_url)
        get_deparment_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url=get_deparment_list_url)
        assert len(list.json()['department']) == 1