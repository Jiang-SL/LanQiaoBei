# -*- coding: utf-8 -*-
# @Time    : 2024/2/1 11:03
# @Author  : Jesse
# @File    : palindrome.py
# @brief   : 1221是一个非常特殊的数，它从左边读和从右边读是一样的，编程求所有这样的四位十进制数。
# @Software: PyCharm

def palindrome():
    for i in range(1000, 10000):
        num_str = str(i)  # 将数字变为字符串
        if num_str == num_str[::-1]:  # 判断数字字符串正反是否一致
            print(i)  # 打印回文数
        else:
            continue


if __name__ == "__main__":
    palindrome()  # 找出所有四位回文数
