# -*- coding: utf-8 -*-
# @Time    : 2024/2/13 9:51
# @Author  : Jesse
# @File    : 快速排序.py
# @brief   : （1）从数列中挑出一个元素，称为 "基准"（pivot）
#         （2）重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
#         在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作
#         （3）递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序
# @Software: PyCharm

def partition(arr, left, right):
    idx = left + 1  # 记录基准值小于等于基准值元素的下标
    for i in range(left + 1, right + 1):
        if arr[i] <= arr[left]:
            arr[idx], arr[i] = arr[i], arr[idx]
            idx += 1
    arr[left], arr[idx - 1] = arr[idx - 1], arr[left]

    return idx - 1  # 返回基准值的下标


def quick_sort(arr, left, right):
    if left < right:  # 确保有两个以上元素能够进行排列，否则结束函数跳出递归
        pivot = partition(arr, left, right)  # 将arr拆分为三部分：左边、基准值、右边，同时返回当前基准值下标
        quick_sort(arr, left, pivot - 1)  # 递归调用，先排序左边
        quick_sort(arr, pivot + 1, right)  # 递归调用，再排序右边


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr) - 1)
    print(" ".join(map(str, arr)))
