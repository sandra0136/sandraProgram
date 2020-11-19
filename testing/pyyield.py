#!/usr/local/bin python3
# -*- coding: utf-8 -*-

def provide():
    for i in range(0,5):
        print("登录")
        yield i #相当于return i,并记录这次的执行位置--总结为：暂停，并下一次继续
        print("退出")

p = provide()
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))

for i in p:
    print(i)

