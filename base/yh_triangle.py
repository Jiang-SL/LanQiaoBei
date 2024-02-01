# -*- coding: utf-8 -*-
# @Time    : 2024/2/1 11:15
# @Author  : Jesse
# @File    : yh_triangle.py
# @brief   : 输出杨辉三角，三角形中的每个数字等于它两肩上的数字相加。
# @Software: PyCharm

def yh_triangle(n):
    triangle = [[0] * n for i in range(n)]  # 初始化n*n的0矩阵

    for i in range(n):
        for j in range(i+1):
            if j == 0 and j == i:
                triangle[i][j] = 1  # 最边边的元素都为1
            else:
                # 两肩之和等于当前的元素
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    else:
        for i in range(n):  # 遍历每一行
            for num in triangle[i]:  # 遍历每一行的各个元素
                if num==0:  # 不输出多余的0
                    break
                else:
                    print(num,end=' ')
            print()  # 换行


if __name__ == "__main__":
    n = int(input())  # 输出n的值，1<=n<=34
    yh_triangle(n)  # 输出杨辉三角
