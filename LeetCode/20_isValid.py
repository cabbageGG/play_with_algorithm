#-*- coding: utf-8 -*-
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {"}":"{","]":"[",")":"("}
        stack = []
        for char in s:
            if char in d.values():
                stack.append(char)
            else:
                if stack == []:
                    return False
                tem = stack.pop()
                if tem != d[char]:
                    return False
        return stack == []