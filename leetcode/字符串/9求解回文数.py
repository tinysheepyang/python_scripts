#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/13 23:27
# @Author  : chenshiyang
# @Site    : 
# @File    : 9求解回文数.py  判断一个数是否是回文数
# @Software: PyCharm

def isPalindrome(n):
    if n < 0:
        return False

    sum = 0
    origin = n


    while n:
        num = n % 10
        sum = sum*10 + num

        n /= 10
    print(sum)
    if sum == origin:
        return True
    else:
        return False

print(isPalindrome(121))