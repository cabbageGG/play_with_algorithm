#-*- coding: utf-8 -*-
'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        l = len(nums)
        results = []
        if l<4 or 4*nums[0] > target or 4*nums[l-1] < target: #这里可以优化：当数组整个最小和大于目标，或最大和小于目标，则不存在。
            return results   
        for i in range(l-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            results = self.threeSum(nums[i+1:],target-nums[i],[nums[i]],results)
            # for ret in rets:  #这里可以优化
            #     results.append([nums[i],ret[0],ret[1],ret[2]])
        return results

    def threeSum(self,nums,target,result,results):
        l = len(nums)
        if l<3:
            return results
        for i in range(l-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            results = self.twoOrderSum(nums[i+1:],target-nums[i],result+[nums[i]],results)
        return results

    def twoOrderSum(self,nums,target,result,results):
        #解决思路：
        #使用两个指针从前后分别开始寻找。
        l = len(nums)
        i = 0
        j = l-1
        while i<j:
            sum = nums[i] + nums[j]
            if sum == target:
                results.append(result+[nums[i],nums[j]])
                i += 1
                j -= 1
                while i<j and nums[i] == nums[i-1]:
                    i += 1
                while i<j and nums[j] == nums[j+1]:
                    j -= 1 
            elif sum > target:
                j -= 1
            else:
                i += 1
        return results  

    # #基于前面的额思考，则可以将问题推广至NSum，其复杂度为O(n^(N-1)) 时间提速3-5倍。
    # def fourSum(self,nums,target):
    #     def findNSum(nums,target,N,result,results):
    #         if len(nums)<N or N<2 or N*nums[0] > target or N*nums[-1] < target: 
    #             return
    #         if N==2:
    #             i,j = 0,len(nums)-1
    #             while i<j:
    #                 sum = nums[i] + nums[j]
    #                 if sum == target:
    #                     results.append(result+[nums[i],nums[j]])
    #                     i += 1
    #                     j -= 1
    #                     while i<j and nums[i] == nums[i-1]:
    #                         i += 1
    #                     while i<j and nums[j] == nums[j+1]:
    #                         j -= 1 
    #                 elif sum > target:
    #                     j -= 1
    #                 else:
    #                     i += 1
    #         else:
    #             for i in range(len(nums)-N+1):
    #                 if i > 0 and nums[i] == nums[i-1]:
    #                     continue
    #                 findNSum(nums[i+1:],target-nums[i],N-1,result+[nums[i]],results)
    #     nums.sort()
    #     results = []
    #     findNSum(nums,target,4,[],results)
    #     return results