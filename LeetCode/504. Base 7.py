#-*- coding: utf-8 -*-
'''
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
'''
class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        flag = False
        if num < 0:
            num = -num
            flag = True
        while num >= 7:
            res = str(num%7) + res
            num = num // 7
        res = str(num) + res
        if flag:
            res = '-' + res
        return res
            