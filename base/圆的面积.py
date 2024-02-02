# -*- coding: utf-8 -*-
# @Time    : 2024/2/2 10:04
# @Author  : Jesse
# @File    : 圆的面积.py
# @brief   : 给定圆的半径r，求圆的面积。 要求结果保留小数点后7位
# @Software: PyCharm

import math


def area(r):
    return math.pi * r * r  # 调用math里面的pi


if __name__ == "__main__":
    r = float(input())
    if r >= 1 and r <= 10000:
        print("%.7f" % area(r))  # 结果保留小数点后7位，四舍五入
