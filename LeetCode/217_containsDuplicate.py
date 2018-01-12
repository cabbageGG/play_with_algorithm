#-*- coding: utf-8 -*-

'''
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
'''
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        l = len(nums)
        for i in range(l):
            if nums[i] in s:
                return True
            else:
                s.add(nums[i])
        return False
