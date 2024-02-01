# -*- coding: utf-8 -*-
# @Time    : 2024/2/1 10:36
# @Author  : Jesse
# @File    : dec2hex.py
# @brief   : 十进制转十六进制
# @Software: PyCharm

dec_num = int(input())
hex_num = hex(dec_num)[2:].upper()  # 将十进制变为十六进制，同时去掉开头的0x，并将其变为大写字母
print(hex_num)
