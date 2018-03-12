#-*- coding: utf-8 -*-

'''
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.
'''


class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # 设计思想：需要用到字符串的切片函数。
        # 遍历一次。
        if A == B:
            return True
        if len(A) != len(B):
            return False
        
        for i in range(len(B)):
            if A != B:
                A = self.shift(A)
            else:
                return True
        return False

    def shift(self,s):
        return s[1:] + s[0]

        

