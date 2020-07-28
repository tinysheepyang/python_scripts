#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 0:38
# @Author  : chenshiyang
# @Site    : 
# @File    : 198-打家劫舍.py
# @Software: PyCharm

arr = [1,2,4,1,7,8,3]

def rec_opt(arr, i):
    if arr is None or len(arr) == 0 or i is None:
        return 0

    if i == 0:
        return arr[0]

    elif i == 1:
        return max(arr[0], arr[1])

    else:
        A = rec_opt(arr, i-2) + arr[i]
        B = rec_opt(arr, i-1)
        return max(A, B)


print(rec_opt(arr, 6))


def dp_opt(arr):
    opt = [0] * len(arr)
    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])

    for i in range(2, len(arr)):
        A = opt[i-2] + arr[i]
        B = opt[i-1]
        opt[i] = max(A, B)

    return opt[len(arr) -1]

def dp_opt1(arr):
    pre, cur = 0, 0

    for i in arr:
        print(i, pre, cur)
        cur , pre = max(pre+i, cur), cur

    return cur

print(dp_opt(arr))
print(dp_opt1(arr))
