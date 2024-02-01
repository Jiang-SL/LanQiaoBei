# -*- coding: utf-8 -*-
# @Time    : 2024/2/1 18:26
# @Author  : Jesse
# @File    : alpha_graph.py
# @brief   :
# 利用字母可以组成一些美丽的图形，下面给出了一个例子：
#           ABCDEFG
#           BABCDEF
#           CBABCDE
#           DCBABCD
#           EDCBABC
# 这是一个5行7列的图形，请找出这个图形的规律，并输出一个n行m列的图形。
# @Software: PyCharm

def alpha_graph(n, m):
    alpha_row = ""  # 一行的字母串
    for i in range(m):
        alpha_row += chr(ord("A") + i)  # 根据m构建初始的字母串，通过ASII码来递增添加

    for i in range(n):
        if i == 0:
            print(alpha_row)  # 第一行直接打印
        else:
            alpha_row = chr(ord(alpha_row[0]) + 1) + alpha_row  # 开头添加一位原第一位ASII码+1的字母
            alpha_row = alpha_row[:-1]  # 去掉最后一位字母  先添加再删除，防止alpha_row为空
            print(alpha_row)  # 打印当前行


if __name__ == "__main__":
    n, m = map(int, input().split())  # 输入n,m
    if n >= 1 and m <= 26:
        alpha_graph(n, m)
