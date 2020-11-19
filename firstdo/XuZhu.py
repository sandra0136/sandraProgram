#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from firstdo.TongLao import TongLao


class XuZhu(TongLao):

    def read(self):
        print("罪过罪过")


tongLao = TongLao(1000, 100)
tongLao.see_people("WYZ")
xuzhu = XuZhu(1000,10)
xuzhu.read()