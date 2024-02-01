# -*- coding: utf-8 -*-
# @Time    : 2024/2/1 17:50
# @Author  : Jesse
# @File    : find_int.py
# @brief   : 给出一个包含n个整数的数列，问整数a在数列中的第一次出现是第几个。
# @Software: PyCharm

def find_int(num_array, num):
    length = len(num_array)  # 数列的长度
    for i in range(length):  # 通过下标遍历数列
        if num_array[i] == num:
            return i + 1  # 返回第一次出现的位置
    else:
        return -1  # 当数列中不存在该数，循环走完才执行，返回-1


if __name__ == "__main__":
    n = int(input())  # 输入n的值
    if n >= 1 and n <= 1000:
        num_array = map(int, input().split())  # 输入一个数列, 拆分每个字符，并转换为int
        num = int(input())  # 输入待查找的整数
        num_array=list(num_array)  # map返回的是迭代器，转换为list
        print(find_int(num_array, num))  # 打印位置
