# -*- coding: utf-8 -*-
# @Time    : 2024/3/4 18:40
# @Author  : isjiangsl@foxmail.com
# @File    : 石子合并.py
# @Brief   : 类似于贪心huffman，每次选择两个合并成一个，保证花费最小
# @Software: PyCharm

import heapq  # 导入堆


def main():
    arr = list(map(int, input().split()))
    result = 0
    heapq.heapify(arr)  # 将原列表变为堆
    while len(arr) >= 2:
        x = heapq.heappop(arr)  # 弹出最小的
        y = heapq.heappop(arr)  # 再弹出最小的
        heapq.heappush(arr, x + y)  # 合并最小的两个，添加到堆中
        result += x + y  # 记录花费
    print(result)


if __name__ == "__main__":
    main()
