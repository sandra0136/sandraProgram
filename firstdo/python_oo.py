#!/usr/local/bin python3
# -*- coding: utf-8 -*-
# 定义类:首字母要大写
# 属性：名词
# 方法：动词
#构造函数的参数，需要在实例化类的时候传递
# 当子类中有和父类重名的方法或者属性，那么首先选择的是子类的

class Bicycle:
    def run(self, km):
        print(f"一共骑行了{km}km")


class EBicycle(Bicycle):
    # 构造函数
    def __init__(self, valume):
        self.valume = valume

    def full_charge(self, vol):
        print(f"电动车已充电{vol}度，充完电还有{vol + self.valume}")

    def run(self, km):
        e_km = self.valume * 10
        if km <= e_km:
            print(f"用电一共骑行{km}")
        else:
            super().run(km)
