#-*- coding: utf-8 -*-
'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
'''
class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # res = sum(int(i) for i in str(num))
        # while res >= 10:
        #     res = sum(int(i) for i in str(res))
        # return res
        return 1 + (num - 1) % 9 #通过列出一些例子找出这个周期性规律。