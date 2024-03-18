# -*- coding: utf-8 -*-
# @Time    : 2024/3/18 17:13
# @Author  : isjiangsl@foxmail.com
# @File    : 拆解数字.py
# @Brief   : 给定一个数字，将其拆分为三个数字，要求后一个大于等于前一个
# @Software: PyCharm

def dfs(num: int, n: int, path: list, depth):
    # depth标识当前处于第depth层
    # 递归出口
    if depth == n:
        # 判断数字是否递增
        for i in range(1, n):
            if path[i] >= path[i - 1]:
                continue
            else:
                return None

        # 判断数字之和是否为x
        if sum(path) != num:
            return None
        print(path)  # 输出拆分结果
        return

    for i in range(1, num + 1):
        path[depth] = i
        dfs(num, n, path, depth + 1)


def main():
    num = int(input())
    n = int(input())
    path = [0] * n


if __name__ == "__main__":
    main()
