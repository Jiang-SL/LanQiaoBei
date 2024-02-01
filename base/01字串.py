# -*- coding: utf-8 -*-
# @Time    : 2024/2/1 19:51
# @Author  : Jesse
# @File    : 01字串.py
# @brief   :
#         问题描述
#         对于长度为5位的一个01串，每一位都可能是0或1，一共有32种可能。它们的前几个是：
#         00000
#         00001
#         00010
#         00011
#         00100
#         请按从小到大的顺序输出这32种01串。
# @Software: PyCharm
def zero_one():
    for i in range(32):  # 0~31依次输出二进制数
        bin_num = bin(i)[2:]  # 去掉开头的0b
        bin_num = bin_num.zfill(5)  # 向右对齐，长度为5，不足就开头补0
        print(bin_num)  # 打印当前的01序列


if __name__ == "__main__":
    zero_one()
