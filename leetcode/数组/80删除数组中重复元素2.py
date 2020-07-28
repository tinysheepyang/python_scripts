#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 17:19
# @Author  : chenshiyang
# @Site    : 
# @File    : 80删除数组中重复元素2.py
# @Software: PyCharm

def removeDuplicates(nums):
    if nums is None:return 0

    i, count = 1,1

    while i < len(nums):
        if nums[i] == nums[i-1]:
            count += 1

            if count > 2:
                nums.pop(i)
                i -= 1

        else:
            count = 1

        i += 1

    return len(nums)


nums = [0,0,1,1,1,1,2,3,3]
print(removeDuplicates(nums))