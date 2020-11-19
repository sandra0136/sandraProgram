#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import requests


class TestToken:

    def test_get_token(self):
        """
        获取token
        :return:
        """
        # 定义凭证
        corpid = "ww2dfe2dadeb083b38"
        corpsecret = '	VD9eqBN3cKwNA-fiJVwDik-ixvGj0lUaB2-bjLCrBYk'
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        # 发get请求
        r = requests.get(url)
        print(r.json())

    def test_token_param(self):
        corpid = "ww2dfe2dadeb083b38"
        corpsecret = 'VD9eqBN3cKwNA-fiJVwDigA1nE-dHes73gVWQUW_rnY'
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        # 定义请求参数
        params = {
            "corpid":corpid,
            "corpsecret":corpsecret
        }
        # 发get请求
        r = requests.get(url,params=params)
        print(r.json())