# -*- coding: utf-8 -*-
# @Time    : 2024/2/1 9:54
# @Author  : Jesse
# @File    : hex2oct.py
# @brief   : 给定n个十六进制正整数，输出它们对应的八进制数。
# @Software: PyCharm

n = int(input())  # 输入n的值
hex = []  # 用于存放n个十六进制数的列表
for i in range(n):  # 输入n个十六进制字符串
    hex.append(int(input(), 16))  # 通过int将每个输入的字符串变为十六进制整型

for num in hex:  # 遍历hex以此换行输出
    print(oct(num)[2:])  # 先将num变为八进制，然后输出，不输出开头的Oo
