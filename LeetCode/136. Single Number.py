#-*- coding: utf-8 -*-
'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # s = set(nums)
        # return 2 * sum(s) - sum(nums)
        #更简单的方法。遍历整个列表，对每个元素进行异或，最后的值就是单个元素的值。
        #因为，相同的元素异或后为0.
        res = 0
        for num in nums:
            res ^= num
        return res