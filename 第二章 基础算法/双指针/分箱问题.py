# -*- coding: utf-8 -*-
# @Time    : 2024/3/5 10:19
# @Author  : isjiangsl@foxmail.com
# @File    : 分箱问题.py
# @Brief   : 贪心思路，双指针
# @Software: PyCharm

def divide_group(gift: list, w: int) -> int:
    gift.sort()  # 排序
    left, right = 0, len(gift) - 1  # 左右指针
    groups = 0  # 分组数目
    while True:
        if left == right:
            groups += 1  # 左右指针相遇时，剩下一个纪念品单独做一组
            break
        elif left > right:
            break  # 左指针超过了右指针，说明已经遍历完，跳出循环
        elif gift[left] + gift[right] <= w:  # 最大的和最小的组合，判断是否超出上限
            left += 1  # 移动左右指针
            right -= 1
            groups += 1  # 满足要求组数加1
        else:  # 不满足要求，移动左右指针
            left += 1
            right -= 1
    return groups


def main():
    w = int(input())  # 价格和上限
    n = int(input())  # 纪念品数目
    gift = []  # 存放纪念品的列表
    for i in range(n):
        gift.append(int(input()))  # 输入n个纪念品价格
    print(divide_group(gift, w))


if __name__ == "__main__":
    main()
