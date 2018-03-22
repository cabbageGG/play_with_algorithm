#-*- coding: utf-8 -*-
'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.


'''
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #将字符串切分成三部分 s1，s2 以及当前字符。如果当前字符不在s1和s2里，则符合条件。
        for i in range(len(s)):
            if s[i] not in s[0:i] and s[i] not in s[i+1:]:
                return i
        return -1
