#-*- coding: utf-8 -*-
'''
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]

'''
class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        for i in range(0,len(s),2*k):
            s1 = s[0:i]
            s2 = s[i:i+k][::-1]
            s3 = s[i+k:]
            s = s1 + s2 + s3
        return s