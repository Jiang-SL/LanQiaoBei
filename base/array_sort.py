# -*- coding: utf-8 -*-
# @Time    : 2024/1/31 13:16
# @Author  : Jesse
# @File    : array_sort.py
# @brief   :给定一个长度为n的数列，将这个数列按从小到大的顺序排列。1<=n<=200
# @Software: PyCharm

n = int(input())  # 输入n
array_input = input()  # 以字符串形式接受n个数字包括了间隔的空格
array = [int(num) for num in array_input.split()]  # 以空格拆分字符串，存入列表

array.sort(reverse=False)

for num in array:
    print(num, end=' ')
