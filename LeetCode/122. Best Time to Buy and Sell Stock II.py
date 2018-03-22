#-*- coding: utf-8 -*-
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #模拟股市的折线图，只买最低点，只买最高点
        if len(prices)<=1:
            return 0
        p = 0
        buy = False
        m1 = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                if not buy:
                    m1 = prices[i]
                    buy = True
            else:
                if buy:
                    p = p + prices[i] - m1
                    buy = False
                    m1 = 0
        if buy:
            p = p + prices[-1] - m1
        return p