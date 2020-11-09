#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/26 23:01
# @Author  : chenshiyang
# @Site    : 
# @File    : 121买卖股票最佳时机.py
# @Software: PyCharm

class Solution:
    def maxProfit(self, prices):
        if prices is None:
            return 0

        minPrices = prices[0]
        maxProfit = 0

        for index, value in enumerate(prices):
            if prices[index] < minPrices:
                minPrices = prices[index]
            elif prices[index] - minPrices > maxProfit:
                maxProfit = prices[index] -minPrices

        return maxProfit


dataList = [7,1,5,3,6,4]

test = Solution()
print(test.maxProfit(dataList))