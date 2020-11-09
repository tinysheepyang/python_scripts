#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/26 23:28
# @Author  : chenshiyang
# @Site    : 
# @File    : 122买卖股票最佳时机.py
# @Software: PyCharm

class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0

        max_profit = 0

        for index in range(1,len(prices)):
            if prices[index] > prices[index-1]:
                print(prices[index], prices[index-1])
                max_profit += prices[index] - prices[index-1]

        return max_profit

prices = [7,1,5,3,6,4]
test = Solution()
print(test.maxProfit(prices))