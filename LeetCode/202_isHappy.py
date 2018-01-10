#-*- coding: utf-8 -*-

'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
'''
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        set_nums = set()
        while n != 1:
            if n not in set_nums:
                set_nums.add(n)
                list_n = [int(i) for i in str(n)]
                n =sum([i*i for i in list_n])
            else:
                return False
        return True


