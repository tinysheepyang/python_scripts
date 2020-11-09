#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/5 23:46
# @Author  : chenshiyang
# @Site    : 
# @File    : 最多能赚几块钱？.py
# @Software: PyCharm

prices = [0, 5, 1, 8, 4, 6, 3, 2, 4]
prev = [0,0,0,0,1,0,2,3,5]

def OPTRecursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 5

    return max(OPTRecursive(n-1), prices[n] + OPTRecursive(prev[n]))


print(OPTRecursive(8))

def OPT(n):

    if n == 0:
        return 0
    if n == 1:
        return 5

    opt = [0] * (n+1)
    opt[0] = 0
    opt[1] = 5

    for i in range(2, n+1):
        opt[i] = max(opt[i-1], opt[prev[i]] + prices[i])

    return opt[n]

print(OPT(8))