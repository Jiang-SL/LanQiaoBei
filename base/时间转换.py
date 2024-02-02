# -*- coding: utf-8 -*-
# @Time    : 2024/2/2 15:46
# @Author  : Jesse
# @File    : 时间转换.py
# @brief   : 给定一个以秒为单位的时间t，要求用“<H>:<M>:<S>”的格式来表示这个时间。
# <H>表示时间，<M>表示分钟，而<S>表示秒，它们都是整数且没有前导的“0”。例如，
# 若t=0，则应输出是“0:0:0”；若t=3661，则输出“1:1:1”
# @Software: PyCharm

def time_convert(second):
    hour = second // 3600  # 取出小时
    second = second - hour * 3600  # 剩余的秒
    minute = second // 60  # 取出分钟
    second = second - minute * 60  # 剩余的秒

    print(hour, end=":")
    print(minute, end=":")
    print(second)


if __name__ == "__main__":
    second = int(input())
    time_convert(second)
