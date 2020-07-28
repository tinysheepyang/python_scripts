#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 23:37
# @Author  : chenshiyang
# @Site    : 
# @File    : 求和.py
# @Software: PyCharm

arr = [3,34,4,12,5,2]

def rec_subset(arr, i, s):

    if s == 0:
        return True
    elif i == 0:
        return arr[0] == s
    elif arr[i] > s:
       return rec_subset(arr, i-1,s)
    else:
        A = rec_subset(arr, i-1, s-arr[i])
        B = rec_subset(arr, i-1, s)

        return A or B

import numpy as np
def dp_subset(arr ,S):
    subset = np.zeros((len(arr),S+1), dtype=bool)
    subset[:,0] = True
    subset[0,:] = False
    subset[0,arr[0]] = True

    for i in range(1, len(arr)):
        for j in range(1, S+1):
            if arr[i] > j:
                subset[i,j] = subset[i-1,j]
            else:
                A = subset[i-1,j-arr[i]]
                B = subset[i-1, j]

                subset[i,j] = A or B
    t,c = subset.shape
    return subset[t-1, c-1]

# print(rec_subset(arr, len(arr)-1, 9))
# print(rec_subset(arr, len(arr)-1, 10))
# print(rec_subset(arr, len(arr)-1, 11))
# print(rec_subset(arr, len(arr)-1, 12))
# print(rec_subset(arr, len(arr)-1, 13))

print(dp_subset(arr, 9))
