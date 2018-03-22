#-*- coding: utf-8 -*-
'''
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.

'''

class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        d = {str(i): nums[i] for i in range(len(nums))} #构造字典
        import collections
        kd = collections.OrderedDict(sorted(d.items(),key=lambda t:t[1],reverse=True)) #对字典的值进行排序，然后放入有序字典，保存这个顺序
        indexs = list(map(int,kd.keys()))
        for i in range(len(indexs)):
            if i == 0:
                nums[indexs[i]] = "Gold Medal" 
            elif i == 1:
                nums[indexs[i]] = "Silver Medal" 
            elif i == 2:
                nums[indexs[i]] = "Bronze Medal" 
            else:
                nums[indexs[i]] = str(i+1)
            
        return nums