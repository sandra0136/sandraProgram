#!/usr/local/bin python3
# -*- coding: utf-8 -*-
class TongLao:
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def see_people(self, name):
        if name == 'WYZ':
            print("师弟！！！！")
        if name == '李秋水':
            print("呸，贱人")
        if name == '丁春秋':
            print("叛徒，我杀了你")

    def fight_zms(self, your_hp, your_power):
        self.hp = self.hp / 2
        self.power = self.power * 10
        self.hp = self.hp - your_power
        your_hp = your_hp - self.power
        if self.hp > your_hp:
            print("我赢了")
        else:
            print("你赢了")

