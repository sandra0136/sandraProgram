#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import requests

from test_requests.api.wework import WeWork


class Department(WeWork):

    def create_department(self, department_id):
        data = {
            "name": "我好",
            "name_en": "wohao",
            "parentid": 1,
            "order": 1,
            "id": department_id
        }
        create_department_url = f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}'
        req = {
            "url": create_department_url,
            "method": "post",
            "json": data
        }
        r = self.send_requests(req)
        return r.json()

    def update_department(self, department_id):
        data = {
            "id": department_id,
            "name": "深圳研发",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }
        update_department_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        req = {
            "method": "post",
            "url": update_department_url,
            "json": data
        }
        r = self.send_requests(req)
        return r.json()

    def delete_department(self, department_id):
        delete_department_url = f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={department_id}'
        req = {
            "method": "get",
            'url': delete_department_url
        }
        r = self.send_requests(req)
        return r.json()

    def get_department_list(self):
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        req = {
            'method': "get",
            "url": get_department_list_url
        }
        dep_list = self.send_requests(req)
        return dep_list.json()
