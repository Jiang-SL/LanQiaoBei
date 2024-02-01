"""
　　输入一个正整数n，输出n!的值。
　　其中n!=1*2*3*…*n。
    n<=1000
"""

n = int(input())  # 输入一个不超过1000的数
result = 1  # 存放计算结果
for i in range(2, n + 1): # 循环计算阶乘
    result *= i

print(result)  # 输出结果
