#-*- coding: utf-8 -*-
'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

'''
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        c = collections.Counter(s)
        res = 0
        for i,v in c.items():
            if v % 2 == 0:
                res += v
            else:
                res += v - 1
        if res < len(s):
            res += 1
        return res
        