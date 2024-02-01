"""
输入A和B,求二者的和
"""


def add(a, b):
    return a + b


a, b = input().split()  # 输入多个数，拆分字符串
a = int(a)  # 转换为int
b = int(b)
print(add(a, b))
