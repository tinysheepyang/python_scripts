#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/23 23:36
# @Author  : chenshiyang
# @Site    : 
# @File    : 268 消失的数字.py
# @Software: PyCharm


"""
题目描述
数组nums包含从0到n的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。你有办法在O(n)时间内完成吗？
"""


class Solution:
    def missingNumber(self, nums) -> int:

        if len(nums) == 0:
            return 0

        missing = 0

        for n in range(len(nums)):
            missing = missing ^ n+1 ^ nums[n]

        return missing

    def missingNumber2(self, nums)-> int:
        count = sum(nums)

        total = (1+len(nums))*len(nums)/2
        return total - count

nums = [9,6,4,2,3,5,7,0,1]
test = Solution()
print(test.missingNumber(nums))
print(test.missingNumber2(nums))