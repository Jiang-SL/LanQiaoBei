# -*- coding: utf-8 -*-
# @Time    : 2024/2/2 15:32
# @Author  : Jesse
# @File    : 字符串对比.py
# @brief   :　
#    给定两个仅由大写字母或小写字母组成的字符串(长度介于1到10之间)，它们之间的关系是以下4中情况之一：
# 　　1：两个字符串长度不等。比如 Beijing 和 Hebei
# 　　2：两个字符串不仅长度相等，而且相应位置上的字符完全一致(区分大小写)，比如 Beijing 和 Beijing
# 　　3：两个字符串长度相等，相应位置上的字符仅在不区分大小写的前提下才能达到完全一致（也就是说，它并不满足情况2）。比如 beijing 和 BEIjing
# 　　4：两个字符串长度相等，但是即使是不区分大小写也不能使这两个字符串一致。比如 Beijing 和 Nanjing
# 　　编程判断输入的两个字符串之间的关系属于这四类中的哪一类，给出所属的类的编号。
# @Software: PyCharm

def str_cmp(str1, str2):
    if str1 == str2:  # 二者完全一致
        result = 2
    elif len(str1) == len(str2) and str1.lower() != str2.lower():  # 长度相等，不区分大小写也不相等
        result = 4
    elif len(str1) == len(str2) and str1.lower() == str2.lower():  # 长度相等，不区分大小写相等
        result = 3
    else:  # 长度不等
        result = 1
    return result


if __name__ == "__main__":
    str1, str2 = (input(), input())
    print(str_cmp(str1, str2))
