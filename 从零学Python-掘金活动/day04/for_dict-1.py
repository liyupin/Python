#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:liyupi
@file: for_dict-1.py
@time: 2022/03/25
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"循环字典的key和value"

# 程序主入口
if __name__ == '__main__':
    # 定义一个字典
    score_dict = {'math': 96, 'english': 97, 'chinese': 98}

    # 循环获取key
    key: str
    for key in score_dict:
        print(key)

    # 循环获取value
    for key in score_dict:
        print(score_dict[key])

    # 循环获取key和value
    for key, value in score_dict.items():
        print(key, value)
