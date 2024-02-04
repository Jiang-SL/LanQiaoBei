# -*- coding: utf-8 -*-
# @Time    : 2024/2/4 10:03
# @Author  : Jesse
# @File    : huffuman树.py
# @brief   : 给定一个数列，求构造huffuman树的总费用
# @Software: PyCharm

def huffuman_cost(num_ary):
    cost = 0
    while len(num_ary) != 1:  # 列表中只有一个元素时结束
        num_ary.sort()  # 升序排序
        num_ary.append(num_ary[0] + num_ary[1])  # 将最小的两个数的和加入列表
        cost += num_ary[0] + num_ary[1]  # 记录总的花费
        num_ary = num_ary[2:]  # 去掉前面两个最小的数
    return cost


if __name__ == "__main__":
    n = int(input())
    if n <= 100:
        num_ary = list(map(int, input().split()))  # 输入一个数列
        if len(num_ary) > n:
            num_ary = num_ary[:n]  # 剔除掉多输入的元素
        print(huffuman_cost(num_ary))
