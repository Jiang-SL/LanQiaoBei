# -*- coding: utf-8 -*-
# @Time    : 2024/2/1 11:08
# @Author  : Jesse
# @File    : special_num.py
# @brief   : 153是一个非常特殊的数，它等于它的每位数字的立方和，即153=1*1*1+5*5*5+3*3*3。(水仙花数)
#            编程求所有满足这种条件的三位十进制数。
# @Software: PyCharm

def daffodil_num():
    for i in range(100, 1000):
        num_str = str(i)
        sum = 0
        for char in num_str:
            sum += int(char) ** 3  # 每个数字的三次方和
        else:
            if sum == i:
                print(i)


if __name__ == "__main__":
    daffodil_num()
