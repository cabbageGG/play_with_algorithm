#-*- coding: utf-8 -*-

'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
'''

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l<=2:
            return l
        #从前往后遍历，将不连续重复2次的元素依次重新赋值给数组的前n位，返回n
        #k:数组中已放好的元素集合，nums[0,k]
        #i:待查找元素起始索引，nums[i,l-1]
        k = 1
        i = 2
        while i<l:
            if nums[i] != nums[k] or nums[i] != nums[k-1]:
                k += 1
                nums[k] = nums[i]
            i += 1
        return k+1

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,2,2,3]
    tt = s.removeDuplicates(nums)
    print (nums,tt)