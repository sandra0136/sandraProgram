#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import requests
from requests.auth import HTTPBasicAuth


def test_auth():
    requests.get(url="https://httpbin.testing-studio.com/basic-auth/banana/123",
                 auth = HTTPBasicAuth("banana","123"))