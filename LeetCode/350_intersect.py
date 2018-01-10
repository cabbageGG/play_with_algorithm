#-*- coding: utf-8 -*-
'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
'''

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = {}
        dict2 = {}
        for num in nums1:
            if num in dict1:
                dict1[num] += 1
            else:
                dict1[num] = 1
        for num in nums2:
            if num in dict2:
                dict2[num] += 1
            else:
                dict2[num] = 1
        set1 = set(dict1.keys()) 
        set2 = set(dict2.keys())
        keys = list(set1 & set2)
        res = []
        for key in keys:
            count = min(dict1[key],dict2[key])
            for i in range(count):
                res.append(key)
        return res
