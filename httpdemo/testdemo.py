#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import json

import requests
from jsonpath import jsonpath
from hamcrest import *
from jsonschema import validate

class TestDemo:
    def test_http(self):
        # 请求目标构造
        r = requests.get("https://httpbin.testing-studio.com/get")
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "level":1,
            "name":"sy"
        }
        r = requests.get("https://httpbin.testing-studio.com/get",params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "sy"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "sy"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['level'] ==1

    def test_hogward_json(self):
        r = requests.get("https://home.testing-studio.com/categories.json")
        print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == '社区治理'
        # jsonpath用于更灵活的定位
        assert jsonpath(r.json(),'$..name')[0] == '社区治理'

    def test_hamcrest(self):
        r = requests.get("https://home.testing-studio.com/categories.json")
        print(r.text)
        assert r.status_code == 200
        assert_that(r.json()['category_list']['categories'][0]['name'],equal_to('社区治理'))
        # jsonpath用于更灵活的定位
        assert jsonpath(r.json(), '$..name')[0] == '社区治理'


    def test_get_login_jsonschema(self):
        url = "https://testerhome.com/api/v3/topics.json"
        data = requests.get(url,params={'limit':'2'}).json()
        schema = json.load(open("topic_shema.json"))
        validate(data,schema=schema)