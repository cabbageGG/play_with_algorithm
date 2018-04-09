#-*- coding: utf-8 -*-
'''
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input: [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Example 2:
Input: [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
'''
class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if not nums:
            return []
        num = nums[0]
        start = False
        for i in range(len(nums)-1):
            if not start:
                num = nums[i]
                start = True
            if nums[i+1] - nums[i] > 1:
                if nums[i] != num:
                    s = str(num)+'->'+str(nums[i])
                    start = False
                    res.append(s)
                else:
                    s = str(nums[i])
                    start = False
                    res.append(s)
        if not start:
            res.append(str(nums[-1]))
        else:
            res.append(str(num)+'->'+str(nums[-1]))
        return res