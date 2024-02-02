# -*- coding: utf-8 -*-
# @Time    : 2024/2/2 9:34
# @Author  : Jesse
# @File    : Fibonacci数列.py
# @brief   : Fibonacci数列的递推公式为：Fn=Fn-1+Fn-2，其中F1=F2=1。
#           当n比较大时，Fn也非常大，现在我们想知道，Fn除以10007的余数是多少。
# @Software: PyCharm

def fibonacii(n):
    f = [0] * n  # 定义一个n长列表用于存放序列
    f[0] = f[1] = 1  # 前两项为1
    for i in range(2, n):
        f[i] = (f[i - 1] + f[i - 2]) % 1007  # 每一项直接求余数即可
    return f[n - 1]  # 返回第n项的余数


if __name__ == "__main__":
    n = int(input())
    if n >= 1 and n <= 1000000:
        print(fibonacii(n))
