# -*- coding: utf-8 -*-
# @Time    : 2024/2/1 18:17
# @Author  : Jesse
# @File    : array_charact.py
# @brief   : 给出n个数，找出这n个数的最大值，最小值，和。
# @Software: PyCharm

def array_charact(num_array):
    print(max(num_array))  # 最大值
    print(min(num_array))  # 最小值
    print(sum(num_array))  # 求和


if __name__ == "__main__":
    n = int(input())
    if n >= 1 and n <= 10000:
        num_array = list(map(int, input().split()))  # 输入n个数
        array_charact(num_array)
