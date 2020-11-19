#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import pytest
import requests


class TestToken:

    @pytest.mark.parametrize("corpid,corpsecret",
                             [("ww2dfe2dadeb083b38","VD9eqBN3cKwNA-fiJVwDigA1nE-dHes73gVWQUW_rnY"),
                              ("","VD9eqBN3cKwNA-fiJVwDigA1nE-dHes73gVWQUW_rnY"),
                              ("ww2dfe2dadeb083b38","")])
    def test_token(self,corpid,corpsecret):
        # corpid = "ww2dfe2dadeb083b38"
        # corpsecret = 'VD9eqBN3cKwNA-fiJVwDigA1nE-dHes73gVWQUW_rnY'
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(token_url)
        print(r.json())
