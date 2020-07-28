#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 13:17
# @Author  : chenshiyang
# @Site    : 
# @File    : 二分查找法.py
# @Software: PyCharm

def BinanySearch(arr, target):

    if arr is None:return -1

    l, r = 0, len(arr)-1 # 在arr[l...r] 中查找target

    while l <= r:
        mid = (l+r)//2
        if arr[mid] == target:
            return mid

        if target > arr[mid]:
            l = mid +1  # target在[mid+1...r]中
        else:
            r = mid -1 # target在[l, mid-1]中

    return -1

arr = [8,9,12,23,34,46,57,68,69,71,82,84,85,89,91,95]

target = BinanySearch(arr, 89)
print(arr[target])
