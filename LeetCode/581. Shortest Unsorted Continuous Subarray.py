#-*- coding: utf-8 -*-
'''
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
'''
class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #超时啦！！改进，先逐个比较，然后在与最小值比较
        L = len(nums)
        iFlag = False
        for i in range(L-1):
            if nums[i] > nums[i+1]:
                iFlag = True
                break
        if not iFlag:
            return 0
        k = 0 #错误的起始索引
        kFlag = False
        min_i = min(nums[i:])
        for k in range(i):
            if nums[k] > min_i:
                kFlag = True
                break
        if not kFlag:
            k = i
            
        for j in range(L-1,0,-1):
            if nums[j] < nums[j-1]:
                break
        k1 = L - 1 #错误的终止索引
        k1Flag = False
        max_j = max(nums[k:j+1])
        for k1 in range(L-1,j,-1):
            if nums[k1] < max_j:
                k1Flag = True
                break
        if not k1Flag:
            k1 = j

        return k1- k + 1
        