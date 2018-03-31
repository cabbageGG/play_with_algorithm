#-*- coding: utf-8 -*-
'''
给定 n 个整数，找出平均数最大且长度为 k 的子数组，并输出该最大平均数。

例:

输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
 

注意:

1 <= k <= n <= 30,000。
所给数据范围 [-10,000，10,000]
'''
class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        i,j,sum_k = 0,k-1,sum(nums[0:k])
        tem_k = sum_k
        for m in range(k,len(nums)):
            tem_k += (nums[m]-nums[m-k])
            sum_k = max(tem_k,sum_k)                
        return sum_k/k
            
        
        
        