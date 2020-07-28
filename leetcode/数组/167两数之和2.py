#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 23:43
# @Author  : chenshiyang
# @Site    : 
# @File    : 167两数之和2.py
# @Software: PyCharm


def twoSum(nums, target):
    """
    双指针实现
    两数之和
    """

    assert len(nums) >= 2

    l, r = 0, len(nums)-1

    while l < r:
        if nums[l] + nums[r] == target:
            return  l+1, r+1

        if nums[r] + nums[l] < target:
            l += 1
        else:
            r -= 1

    print('The input has no solution')

def twoSum1(nums, target):
    """
    二分查找法
    两数之和
    """

    assert len(nums) >= 2

    for i in nums:
        second_num = target - nums[i]
        l, r = 0, len(nums) -1

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == second_num:
                return i+1, mid+1

            if nums[mid] < second_num:
                l = mid +1
            else:
                r = mid -1

    print('The input has no solution')

numbers = [2,7,8,12,15,19,21]
print(twoSum1(numbers, 27))