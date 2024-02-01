# -*- coding: utf-8 -*-
# @Time    : 2024/2/1 10:45
# @Author  : Jesse
# @File    : special_palindrome.py
# @brief   : 123321是一个非常特殊的数，它从左边读和从右边读是一样的。
# 　　        输入一个正整数n， 编程求所有这样的五位和六位十进制数，满足各位数字之和等于n 。
# @Software: PyCharm

def special_palindrome(n):
    for i in range(10000, 1000000):
        num_str = str(i)
        if num_str == num_str[::-1]:  # 判断字符串与其反转字符串是否一致
            sum = 0  # 用于求每个数字的和
            for char in num_str:
                sum += int(char)
            if sum == n:
                print(i)


if __name__ == "__main__":
    n = int(input())  # 输出一个正整数n
    special_palindrome(n)  # 找出符合要求的回文数
