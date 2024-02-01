# -*- coding: utf-8 -*-
# @Time    : 2024/2/1 20:07
# @Author  : Jesse
# @File    : 闰年判断.py
# @brief   :
#     给定一个年份，判断这一年是不是闰年。
#     当以下情况之一满足时，这一年是闰年：
#     1. 年份是4的倍数而不是100的倍数；
#     2. 年份是400的倍数。
#     其他的年份都不是闰年。
# @Software: PyCharm

import calendar


def is_year_leap(year):
    return calendar.isleap(year)  # 直接调用calender模块来判断闰年，Python牛逼！


if __name__ == "__main__":
    year = int(input())
    if year>=1990 and year<=2050:
        if(is_year_leap(year)):
            print("yes")
        else:
            print("no")
