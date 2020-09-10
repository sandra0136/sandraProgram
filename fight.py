#!/usr/local/bin python3
# -*- coding: utf-8 -*-
def fight():
    my_hp = 1000
    my_power = 100
    your_hp = 1000
    your_power = 100

    while True:
        my_hp = my_hp - your_power
        your_hp = your_hp - my_power
        if my_hp <= 0:
            print("你赢了")
            print(f"我的血槽{my_hp},你的血槽{your_hp}")
            break
        elif your_hp <= 0:
            print('我赢了')
            break
fight()