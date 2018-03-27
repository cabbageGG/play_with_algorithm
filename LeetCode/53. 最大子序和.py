#-*- coding: utf-8 -*-
'''
给定一个序列（至少含有 1 个数），从该序列中寻找一个连续的子序列，使得子序列的和最大。

例如，给定序列 [-2,1,-3,4,-1,2,1,-5,4]，
连续子序列 [4,-1,2,1] 的和最大，为 6。
'''

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        _sum = 0
        _max = nums[0]
        start = False
        for num in nums:
            if not start and num > 0:
                start = True
            if start:
                _sum += num
                _max = max(_max,_sum)
            if _sum < 0:
                _sum = 0
                start = False
            _max = max(_max,num)
        return _max
                
                
        