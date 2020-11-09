#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/23 23:04
# @Author  : chenshiyang
# @Site    : 
# @File    : 169多数元素.py
# @Software: PyCharm


"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。


算法描述
摩尔投票法（Boyer–Moore majority vote algorithm），也被称作「多数投票法」，算法解决的问题是：如何在任意多的候选人中（选票无序），选出获得票数最多的那个。

算法可以分为两个阶段：

对抗阶段：分属两个候选人的票数进行两两对抗抵消
计数阶段：计算对抗结果中最后留下的候选人票数是否有效
这样说比较抽象，我们直接来看一道题：LeetCode 169. 多数元素


投票法思路
根据上述的算法思想，我们遍历投票数组，将当前票数最多的候选人与其获得的（抵消后）票数分别存储在 major 与 count 中。

当我们遍历下一个选票时，判断当前 count 是否为零：

若 count == 0，代表当前 major 空缺，直接将当前候选人赋值给 major，并令 count++
若 count != 0，代表当前 major 的票数未被完全抵消，因此令 count--，即使用当前候选人的票数抵消 major 的票数

"""



class Solution:
    def majorityElement(self, nums) -> int:

        if len(nums) == 0 or nums is None:
            return 0

        major = 0
        count = 0

        for n in nums:
            if count == 0:
                major = n

            if major == n:
                count += 1
            else:
                count -= 1
        return major

nums = [2,2,1,1,1,2,2]
test = Solution()
print(test.majorityElement(nums))