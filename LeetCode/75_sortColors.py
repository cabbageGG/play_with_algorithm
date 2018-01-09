#-*- coding: utf-8 -*-
'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
'''

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        colors = [0,0,0]
        #可以使用计数方法来统计颜色
        i = 0
        while i<l:
            if nums[i] == 0:
                colors[0] += 1
            elif nums[i] == 1:
                colors[1] += 1
            else:
                colors[2] += 1
            i += 1
        index = 0
        for j in range(len(colors)):
            for k in range(colors[j]):
                nums[index] = j
                index += 1
        


if __name__ == '__main__':
    s = Solution()
    nums = [1]
    tt = s.sortColors(nums)
    print (nums,tt)
    
