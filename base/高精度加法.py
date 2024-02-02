# -*- coding: utf-8 -*-
# @Time    : 2024/2/2 10:31
# @Author  : Jesse
# @File    : 高精度加法.py
# @brief   : 输入两个整数a和b，输出这两个整数的和。a和b都不超过100位。
# @Software: PyCharm

def big_add(a, b):
    return a + b  # python不需要考虑精度，牛逼！


if __name__ == "__main__":
    a, b = (int(input()), int(input()))  # 回车方式输入两个数
    print(big_add(a, b))
