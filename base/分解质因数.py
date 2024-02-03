# -*- coding: utf-8 -*-
# @Time    : 2024/2/2 15:56
# @Author  : Jesse
# @File    : 分解质因数.py
# @brief   : 求出区间[a,b]中所有整数的质因数分解。
# @Software: PyCharm

def check_prime(num):  # 判断是否为素数
    if num < 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:  # 从2开始，到num-1，判断是否存在因子
                return False
        else:
            return True


def decompose(a, b):
    for i in range(a, b + 1):
        if check_prime(i):
            print(f"{i}={i}")
        else:
            temp = i
            print(f"{i}=", end="")
            j = 2
            while True:  # 每次从最小的质数开始，寻找质因子
                if temp % j == 0 and check_prime(j):  # j是否为质因子
                    temp = temp // j  # 整除质因子
                    print(j, end="*")  # 打印质因子
                    j = 2  # 再次令j为最小的质数
                    if check_prime(temp):  # 余数为质数时，打印余数并结束循环
                        print(temp)
                        break
                else:
                    j += 1


if __name__ == "__main__":
    a, b = map(int, input().split())
    decompose(a, b)
