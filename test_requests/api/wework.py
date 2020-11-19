#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import requests

from test_requests.api.baseapi import BaseApi


class WeWork(BaseApi):

    def get_token(self,corpsecret):
        # token定义
        corpid = "ww2dfe2dadeb083b38"
        # corpsecret = 'VD9eqBN3cKwNA-fiJVwDigA1nE-dHes73gVWQUW_rnY'
        # get_token 的请求信息
        req = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        }
        # token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        # r = requests.get(url=token_url)
        r = self.send_requests(req)
        self.token = r.json()['access_token']
        return self.token
