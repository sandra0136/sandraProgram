#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import requests

class TestCookies:
    def test_cookie1(self):
        url = "https://httpbin.testing-studio.com/cookies"
        header = {
            "Cookie":"hogwards=school",
            'User-Agent': 'hogwards'
        }
        r = requests.get(url,headers=header)
        print(r.request.headers)

    def test_cookie2(self):
        url = "https://httpbin.testing-studio.com/cookies"
        header = {
            'User-Agent': 'hogwards'
        }
        cookie_data = dict(hogwards='school')
        r = requests.get(url, headers=header,cookies=cookie_data)
        print(r.request.headers)
