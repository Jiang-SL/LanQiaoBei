# -*- coding: utf-8 -*-
# @Time    : 2024/3/1 16:55
# @Author  : isjiangsl@foxmail.com
# @File    : 桶排序.py
# @Brief   : 在额外空间充足的情况下，尽量增大桶的数量
#            使用的映射函数能够将输入的 N 个数据均匀的分配到 K 个桶中
#            然后对每个桶内进行排序
# @Software: PyCharm

def bucket_sort(arr: list, bucket_count: int):
    min_value, max_value = min(arr), max(arr)  # 获取最大值和最小值
    bucket_size = (max_value - min_value + 1) // bucket_count  # 计算桶的数量
    bucket_size = max(1, bucket_size)  # 确保至少有个1个桶，避免除零错误
    buckets = [[] for _ in range(bucket_count + 1)]  # 创建bucket_count个桶

    for elem in arr:
        idx = (elem - min_value) // bucket_size
        buckets[idx].append(elem)

    result = []
    for bucket in buckets:
        bucket.sort()
        result += bucket

    return result


def main():
    bucket_count = int(input())
    # arr = [4, 3, 2, 1, 9, 8, 6, 5, 7]
    arr = list(map(int, input().split()))
    arr = bucket_sort(arr, bucket_count)  # 桶排序
    print(' '.join(map(str, arr)))  # 打印结果


if __name__ == "__main__":
    main()
