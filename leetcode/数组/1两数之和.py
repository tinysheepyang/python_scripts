#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 17:10
# @Author  : chenshiyang
# @Site    : 
# @File    : 1两数之和.py
# @Software: PyCharm

def twoSum(nums, target):

    num1 = 0
    for i in nums:
        num1 = target - i

        if num1 in nums:
            return [ nums.index(i), nums.index(num1)]

    return []

nums = [2, 7, 11, 15]
print(twoSum(nums, 22))