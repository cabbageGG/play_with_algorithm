#-*- coding: utf-8 -*-
'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #这种多的Sum的问题，通常需要降维至2Sum问题来解决。
        nums.sort()
        sum = nums[0]+nums[1]+nums[2]
        l = len(nums)
        if l < 3:
            return -1
        for i in range(l-2):
            tem = self.twoSumClosest(nums[i+1:],target-nums[i])
            if abs(tem+nums[i]-target) < abs(sum-target):
                sum = tem + nums[i]
        return sum
    
    def twoSumClosest(self,nums,target):
        l,r = 0,len(nums)-1
        sum = nums[0] + nums[-1]
        while l<r:
            tem = nums[l] + nums[r]
            if tem == target:
                return tem
            elif tem > target:
                r -= 1 
            else:
                l += 1  
            if abs(tem-target) < abs(sum-target):
                sum = tem                
        return sum

