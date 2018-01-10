#-*- coding: utf-8 -*-

'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
'''

class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split(' ')
        if len(pattern) != len(str_list) or len(set(pattern)) != len(set(str_list)):
            return False
        d = {}
        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]] = str_list[i]
            elif d[pattern[i]] != str_list[i]:
                return False
        return True
        
                