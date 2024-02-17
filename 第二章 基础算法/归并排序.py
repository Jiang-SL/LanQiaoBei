# -*- coding: utf-8 -*-
# @Time    : 2024/2/16 16:59
# @Author  : Jesse
# @File    : 归并排序.py
# @brief   :
# @Software: PyCharm

def merge(arr_a, arr_b):
    """将两个有序数组合并成一个新的有序数组"""
    result = []
    while len(arr_a) != 0 and len(arr_b) != 0:  # 二者都非空时
        if arr_a[0] <= arr_b[0]:
            result.append(arr_a.pop(0))  # 弹出arr_a中的最小元素并追加到result
        else:
            result.append(arr_b.pop(0))  # 弹出最小值，追加到result

    result.extend(arr_a)  # arr_a和arr_b中有一个为空，直接将两个添加进去，免去判断
    result.extend(arr_b)  # extend将一个序列追加到一个列表后面
    return result


def mere_sort(arr):
    if len(arr) < 2:  # 数组中只有一个元素时，结束
        return arr
    else:
        mid = len(arr) // 2  # 获取数组中间位置下标
        left_arr = mere_sort(arr[:mid])  # 排序左边子数组
        right_arr = mere_sort(arr[mid:])  # 排序右边子数组
    return merge(left_arr, right_arr)  # 将左右两个数组合并为一个有序数组


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    arr = mere_sort(arr)
    print(" ".join(map(str, arr)))
