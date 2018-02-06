#-*- coding: utf-8 -*-
'''
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
'''

class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        #由于python取反运算符是有符号的额。
        #这里使用异或运算，来得到反码。
        #如：5：101
        #则 111 ^ 101 = 010 即得到5的反码
        mask = 1
        while mask <= num:
            mask <<= 1
        mask -= 1
        return mask ^ num

s = Solution()
s.findComplement(5)
        
        
