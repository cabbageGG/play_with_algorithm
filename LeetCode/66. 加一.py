#-*- coding: utf-8 -*-
'''
给定一个非负整数组成的非空数组，给整数加一。

可以假设整数不包含任何前导零，除了数字0本身。

最高位数字存放在列表的首位。
'''
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a = 0
        for i in digits:
            a = a* 10 + i
        a += 1
        return [int(i) for i in list(str(a))]