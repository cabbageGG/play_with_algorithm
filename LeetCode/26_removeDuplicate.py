#-*- coding: utf-8 -*-
'''
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
'''

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l<=1:
            return l
        #从前往后遍历，将不重复的元素依次重新赋值给数组的前n位，返回n
        #k:数组中已放好的元素集合，nums[0,k]
        #i:待查找元素起始索引，nums[i,l-1]
        k = 0
        i = 0
        while i<l:
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
            i += 1
        return k+1


if __name__ == '__main__':
    s = Solution()
    nums = []
    tt = s.removeDuplicates(nums)
    print (nums,tt)