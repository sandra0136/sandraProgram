#!/usr/local/bin python3
# -*- coding: utf-8 -*-
import json

dict_hogwarts = {
    'a' : [1, 2, 3],
    'name' : ['sprider man', '星矢']
     }
# 在data.json当中写入python object 数据
# with open("data.json", 'w') as f:
    # json.dump表示把python对象写入文件中
    # json.dump(dict_hogwarts, f, ensure_ascii=False )
print(type(dict_hogwarts))
# json.dumps表示把python对象，转化成字符串
print(type(json.dumps(dict_hogwarts)))
