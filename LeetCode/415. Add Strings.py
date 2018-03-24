#-*- coding: utf-8 -*-
'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = ''
        flag = 0
        L1 = len(num1)
        L2 = len(num2)
        if L1 < L2:
            for i in range(-1,-L1-1,-1):
                tem = int(num1[i]) + int(num2[i]) + flag
                if tem >= 10:
                    tem -= 10
                    flag = 1
                else:
                    flag = 0
                res = str(tem) + res
            for i in range(-L1-1,-L2-1,-1):
                tem = int(num2[i]) + flag
                if tem >= 10:
                    tem -= 10
                    flag = 1
                else:
                    flag = 0
                res = str(tem) + res
        else:
            for i in range(-1,-L2-1,-1):
                tem = int(num1[i]) + int(num2[i]) + flag
                if tem >= 10:
                    tem -= 10
                    flag = 1
                else:
                    flag = 0
                res = str(tem) + res
            for i in range(-L2-1,-L1-1,-1):
                tem = int(num1[i]) + flag
                if tem >= 10:
                    tem -= 10
                    flag = 1
                else:
                    flag = 0
                res = str(tem) + res
        if flag:
            res = '1' + res
        return res
            