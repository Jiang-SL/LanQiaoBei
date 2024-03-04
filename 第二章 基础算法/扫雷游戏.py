# -*- coding: utf-8 -*-
# @Time    : 2024/3/4 10:11
# @Author  : isjiangsl@foxmail.com
# @File    : 扫雷游戏.py
# @Brief   :
# @Software: PyCharm

def input_list():
    """以空格分割键入一个列表 """
    return list(map(int, input().split()))


def output_matrix(matrix):
    """打印一个矩阵"""
    for row in matrix:
        print(' '.join(map(str, row)))  # 输出每一行


def detect_mine(chess_board: list, n: int, m: int) -> list:
    result = [[0] * m for _ in range(n)]  # 构建并初始化结果棋盘
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)]  # 定义八个方向
    for i in range(n):
        for j in range(m):
            if chess_board[i][j] == 1:
                result[i][j] = 9  # 如果该位置有地雷则标为9
            else:
                for direction in directions:
                    x, y = i + direction[0], j + direction[1]  # 移动的坐标，行和列加上对应的方向，等于新坐标
                    if 0 <= x < n and 0 <= y < m:  # 保证坐标在允许范围内
                        result[i][j] += chess_board[x][y]  # 由于地雷是1，初始的result格子是0，累加即可统计周围的地雷数
    return result


def main():
    n, m = input_list()  # 输入行列数n, m
    chess_board = []  # 扫雷棋盘
    for i in range(n):
        chess_board.append(input_list())  # 输入扫雷棋盘
    result = detect_mine(chess_board, n, m)  # 扫雷
    output_matrix(result)  # 打印结果


if __name__ == "__main__":
    main()
