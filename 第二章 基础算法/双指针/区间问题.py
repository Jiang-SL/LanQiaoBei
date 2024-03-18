# -*- coding: utf-8 -*-
# @Time    : 2024/3/5 10:47
# @Author  : isjiangsl@foxmail.com
# @File    : 区间问题.py
# @Brief   : 双指针同向扫描，控制一个滑动窗口
# @Software: PyCharm

def beautiful_interval(arr: list, n: int, S: int) -> int:
    min_len = n + 1
    left, right = 0, 0  # 两个同向指针的初始化,定义区间[left,right)

    interval_sum = 0  # 区间和
    while left < n:
        while right < n and interval_sum < S:
            interval_sum += arr[right]
            right+=1


def main():
    n, S = map(int, input().split())  # 序列的长度n和常数S
    arr = list(map(int, input().split()))  # 输入n长的序列




if __name__ == "__main__":
    main()
