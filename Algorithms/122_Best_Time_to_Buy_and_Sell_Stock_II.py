#! /usr/bin/env python
# coding: utf-8


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if not prices or len(prices) < 2:
            return profit

        prev = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > prev:
                profit += prices[i] - prev

            prev = prices[i]

        return profit
