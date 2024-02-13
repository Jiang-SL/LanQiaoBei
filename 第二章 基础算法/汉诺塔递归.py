# -*- coding: utf-8 -*-
# @Time    : 2024/2/13 10:37
# @Author  : Jesse
# @File    : 汉诺塔递归.py
# @brief   : 经典汉诺塔问题，使用递归实现
# @Software: PyCharm

def hanoi_move(n, a, b, c):
    if n == 0:  # 递归终止条件
        return
    hanoi_move(n - 1, a, c, b)  # 将n-1个盘子从a移动到b借助c
    print(f"{a}->{c}")  # 输出a移动到c
    hanoi_move(n - 1, b, a, c)  # 将n-1个盘子再从b移动到c借助b


if __name__ == "__main__":
    n = int(input())
    hanoi_move(n, "A", "B", "C")
