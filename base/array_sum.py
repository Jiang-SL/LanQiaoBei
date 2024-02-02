# -*- coding: utf-8 -*-
# @Time    : 2024/2/2 10:18
# @Author  : Jesse
# @File    : array_sum.py
# @brief   : 求1+2+3+...+n的值。
# @Software: PyCharm

def array_sum(n):
    return int((1 + n) * n / 2)  # 等差数列前n项和


if __name__ == "__main__":
    n = int(input())
    if n >= 1 and n <= 1000000000:
        print(array_sum(n))
