# -*- coding: utf-8 -*-
# @Time    : 2024/2/11 10:47
# @Author  : Jesse
# @File    : 插入排序.py
# @brief   : 第一个元素看做已排序，从左向右遍历每一个元素
#            在已排序元素中从后往前扫描：如果当前元素大于新元素，则该元素移动到后一位
#            重复第二步直至找到小于等于新元素则停止
# @Software: PyCharm

def insert_sort(num_array):
    length = len(num_array)
    for i in range(1, length):  # 从前往后遍历每个元素
        value = num_array[i]  # value用于记录需要待插入的元素，防止被覆盖
        for j in range(i - 1, -1, -1):  # 从已排序元素中，从后向前遍历
            if num_array[j] > value:  # 当前元素大于待排序元素
                num_array[j + 1] = num_array[j]  # 当前元素向后移
            else:  # 当前元素小于或者等于待排序元素时
                num_array[j + 1] = value  # 将待插入元素插入当前元素后面一个位置
                break  # 跳出循环，进行下一个元素的插入


if __name__ == "__main__":
    num_array = list(map(int, input().split()))
    insert_sort(num_array)
    print(" ".join(map(str, num_array)))  # 将列表中每个元素转换为str，然后通过空格连接
