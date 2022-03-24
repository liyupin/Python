#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:liyupi
@file: calc-1.py
@time: 2022/03/24
"""
# 程序主入口
if __name__ == '__main__':
    # 运算方式
    operate_type = input('请选择运算类型：1加法，2减法，3乘法，4除法：')
    while int(operate_type) not in (1, 2, 3, 4):
        print('类型选择错误，只能1~4')
        operate_type = input('请重新选择运算类型：1加法，2减法，3乘法，4除法：')
    num_1 = int(input('请输入第一个数'))
    num_2 = int(input('请输入第二个数'))
    if operate_type == '1':
        rerult = num_1 + num_2
        print('加法结果：' + str(rerult))
    if operate_type == '2':
        rerult = num_1 - num_2
        print('减法结果：' + str(rerult))
    if operate_type == '3':
        rerult = num_1 * num_2
        print('乘法结果：' + str(rerult))
    if operate_type == '4':
        rerult = num_1 / num_2
        print('除法结果：' + str(rerult))
