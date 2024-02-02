# -*- coding: utf-8 -*-
# @Time    : 2024/2/2 10:37
# @Author  : Jesse
# @File    : 报时助手.py
# @brief   : 给定当前的时间，请用英文的读法将它读出来。
# @Software: PyCharm
num_dir = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
           9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
           15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
           30: "thirty", 40: "forty", 50: "fifty"}


def read_time(h, m):
    if m == 0:
        if h <= 20:
            time_result = num_dir[h] + " " + "o'clock"
        else:
            time_result = num_dir[20] + " " + num_dir[h - 20] + " " + "o'clock"
    else:
        if h <= 20:
            if m <= 20:
                time_result = num_dir[h] + " " + num_dir[m]
            else:
                # 将分钟的十位和各位取出来分开读
                time_result = num_dir[h] + " " + num_dir[(m // 10) * 10] + " " + num_dir[m - (m // 10) * 10]
        else:
            if m <= 20:
                time_result = num_dir[20] + " " + num_dir[h - 20] + " " + num_dir[m]
            else:
                # 将小时和分钟的十位与各位取出来分开读
                time_result = num_dir[20] + " " + num_dir[h - 20] + " " + num_dir[(m // 10) * 10] + " " + num_dir[
                    m - (m // 10) * 10]

    return time_result


if __name__ == "__main__":
    h, m = map(int, input().split())  # 输入时和分，空格分隔
    print(read_time(h, m))
