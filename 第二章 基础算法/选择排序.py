# -*- coding: utf-8 -*-
# @Time    : 2024/2/11 21:14
# @Author  : Jesse
# @File    : 选择排序.py
# @brief   : 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
#           再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
#           重复第二步，直到所有元素均排序完毕
# @Software: PyCharm

def selection_sort(arr):
    length = len(arr)  # 数列长度
    for i in range(length):  # 遍历所有元素
        min_idx = i  # 最小元素下标
        for j in range(i + 1, length):  # 从i+1开始，遍历剩余元素
            if arr[min_idx] > arr[j]:
                min_idx = j  # 更新最小下标
        else:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 最小元素和当前元素交换


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    selection_sort(arr)
    print(" ".join(map(str, arr)))  # 以空格连接每个元素，然后打印
