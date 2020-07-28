#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 16:46
# @Author  : chenshiyang
# @Site    : 
# @File    : 26移除重复元素.py
# @Software: PyCharm

nums = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums) -> int:
    if nums is None:return 0

    p ,q = 0, 1
    while q < len(nums):
        if nums[p] != nums[q]:
            nums[p+1] = nums[q]
            p += 1

        q += 1

    return p+1

print(removeDuplicates(nums))

