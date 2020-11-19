#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import json

import yaml
from jsonpath import jsonpath
from jsonschema import validate

from test_requests.api.department import Department


class TestDepartment:
    def setup_class(self):
        # wework = WeWork()
        self.department = Department()
        config_info = yaml.safe_load(open("./config.yaml"))
        # 通过传入不同的secret获取不同的token权限
        self.department.get_token(config_info['token']['department_secret'])

    def test_create_department(self):
        self.department.create_department(3)
        dep_list = self.department.get_department_list()
        names = self.department.base_jsonpath(dep_list,"$..name")
        assert "我好" in names

    def test_update_department(self):
        self.department.update_department(3)
        dep_list = self.department.get_department_list()
        names = self.department.base_jsonpath(dep_list, "$..name")
        assert "深圳研发" in names

    def test_delete_department(self):
        self.department.delete_department(3)
        dep_list = self.department.get_department_list()
        department_ids = self.department.base_jsonpath(dep_list,"$..id")
        assert 3 not in department_ids

    def test_get_department_list(self):
        r = self.department.get_department_list()
        get_list_schema = json.load(open("./jsonschema/get_list_schema.json"))
        # validate(r,get_list_schema)
        self.department.base_jsonschema(r,get_list_schema)