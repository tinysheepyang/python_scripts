#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/9 23:23
# @Author  : chenshiyang
# @Site    : 
# @File    : 求相邻最大和.py
# @Software: PyCharm

arry = [1,2,4,1,7,8,3]

def OPT(n):

    if n == 0:
        return arry[0]

    if n == 1:
        return max(arry[0], arry[1])

    return max(OPT(n-1), arry[n]+OPT(n-2))

print(OPT(6))

def dp_opt(arr):
    import numpy as np

    opt = np.zeros(len(arr))
    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])

    for i in range(2, len(arr)):
        a = opt[i-1]
        b = arr[i] + opt[i-2]
        opt[i] = max(a, b)

    print(opt)
    return opt[len(arr) -1]

print(dp_opt(arry))