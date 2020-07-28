#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 15:35
# @Author  : chenshiyang
# @Site    : 
# @File    : 23移除元素.py
# @Software: PyCharm


nums = [0,1,2,2,3,0,4,2]

def remove_element(nums, val):

    if nums is None:return -1
    if val is None or not isinstance(val, int):return -1

    k = 0
    for i in nums:
        if i != val:
            nums[k] = i
            k += 1
    return k

# print(remove_element(nums, 2))

def remove_element1(nums, val):

    i = 0
    ans = len(nums)
    while i < ans:
        if nums[i] == val:
            print('i----',nums[i])
            print('ans--',nums[ans-1])
            nums[i] = nums[ans-1]
            ans -= 1
        else:
            i += 1

    print(nums)
    return ans

print(remove_element1(nums, 2))
