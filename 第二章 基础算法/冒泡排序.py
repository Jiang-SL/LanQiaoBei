# -*- coding: utf-8 -*-
# @Time    : 2024/2/11 20:47
# @Author  : Jesse
# @File    : 冒泡排序.py
# @brief   : 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
#             对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
#             针对所有的元素重复以上的步骤，除了最后一个。
#             持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较
# @Software: PyCharm

def bubble_sort(num_array):
    length = len(num_array)
    for i in range(0, length - 1):  # 从0开始，遍历length-1个元素
        for j in range(length - i - 1):  # 外层循环从0开始就内层循环要-1，如果从1开始则不用-1
            if num_array[j] > num_array[j + 1]:  # 前面的比后面大，交换两个元素
                temp = num_array[j]
                num_array[j] = num_array[j + 1]
                num_array[j + 1] = temp
                # num_array[j],num_array[j+1]=num_array[j+1],num_array[j]  # 可以这样子交换


if __name__ == "__main__":
    num_array = list(map(int, input().split()))
    bubble_sort(num_array)
    print(" ".join(map(str, num_array)))  # 以空格连接了列表每个元素，形成一个字符串输出
