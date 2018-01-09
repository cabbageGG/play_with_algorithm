#-*- coding: utf-8 -*-

'''
Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.
'''

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = len(nums)
        #从前到后遍历数组，将数组中符合条件的元素重新赋值给数组的前n位。
        #k:记录第一个不符合条件的元素,nums[0,k)符合条件；
        #i:记录待考察元素,nums[i,l-1]待考察。若元素不为零，则直接赋值给k索引的元素，k++。
        k = 0
        i = 0
        while i<l:
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
            i += 1 
        return k

if __name__=='__main__':
    s = Solution()
    nums = [2]
    val = 4
    tt = s.removeElement(nums,val)
    print (nums,tt)

