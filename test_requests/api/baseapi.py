#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import requests
from jsonpath import jsonpath
from jsonschema import validate


class BaseApi:

    def send_requests(self,req:dict):
        """
        对requests进行二次封装
        :return:
        """
        # req = {
        #     "method":"get",
        #     "url":"xxxx",
        #     "params":{},
        #     "json":{}
        # }
        # 等同于 requests.request(method=get,url="xxxx",params={},jsom={})
        return requests.request(**req)

    def base_jsonpath(self,obj,json_expr):
        return jsonpath(obj,json_expr)

    def base_jsonschema(self,instance,schema):
        return validate(instance,schema)