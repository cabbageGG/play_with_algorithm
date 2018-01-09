#-*- coding: utf-8 -*-

'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

'''

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        #从前到后遍历数组，将数组中符合条件的元素重新赋值给数组的前n位。
        #k:记录新正确数组的索引；i：记录考察元素,若元素不为零，则直接赋值给k索引的元素，k++。
        i = 0
        k = 0
        while i<l:
            if nums[i]:
                nums[k] = nums[i]
                k += 1
            i += 1
        while k<l:
            nums[k] = 0
            k += 1

if __name__=='__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    print (nums)
            
