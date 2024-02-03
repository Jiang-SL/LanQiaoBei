# -*- coding: utf-8 -*-
# @Time    : 2024/2/3 11:13
# @Author  : Jesse
# @File    : 矩阵乘法.py
# @brief   : 给定一个N阶矩阵A，输出A的M次幂（M是非负整数
# @Software: PyCharm

from copy import deepcopy


def matrix_multip(matrix1, matrix2):  # 矩阵相乘函数
    row1, cols1 = (len(matrix1), len(matrix1[0]))  # 获取第一个矩阵的行数和列数
    row2, cols2 = (len(matrix2), len(matrix2[0]))

    # 推导式创建一个n*n,元素都为0的列表模拟矩阵
    result = [[0 for _ in range(cols2)] for _ in range(row1)]

    for i in range(0, row1):  # 根据矩阵乘法规则，相乘
        for j in range(0, cols2):
            for k in range(0, cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]  # 矩阵相乘操作，关键！
    return result


def matrix_exponent(matrix, M):  # 求矩阵的M次幂
    if M == 0:
        # 矩阵的0次幂是单位阵，所以构建一个单位阵
        result = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == j:
                    result[i][j] = 1  # 对角线为1
                else:
                    result[i][j] = 0  # 其他位置为0
    else:
        result = deepcopy(matrix)  # 深拷贝matrix
        for i in range(0, M - 1):
            result = matrix_multip(result, matrix)  # 矩阵相乘
    return result


def print_matrix(matrix):  # 打印矩阵的函数
    for row in matrix:  # 遍历每行
        for cols in row:  # 遍历每行中的列
            print(cols, end=' ')
        else:
            print()  # 打印完一行换行


if __name__ == "__main__":
    N, M = map(int, input().split())  # 输入矩阵的阶数和幂次
    if (N >= 1 and N <= 30) and (M >= 0 and M <= 5):
        matrix = []
        for i in range(N):  # 输入N阶矩阵
            matrix.append(list(map(int, input().split())))
        print_matrix(matrix_exponent(matrix, M))
