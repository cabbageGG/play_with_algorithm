#-*- coding: utf-8 -*-
'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
'''

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        #使用滑动窗口查找，初始窗口为0.将滑动窗口里的值插入查找表。
        l = len(nums)
        i,j = 0,0
        s = set()
        if k==0:
            return False
        #建立初始查找表
        while j<k and j<l:
            if nums[j] not in s:
                s.add(nums[j])
                j += 1
            else:
                return True
        while j<l:
            if nums[j] not in s:
                s.add(nums[j])
                if nums[i] in s:   
                    s.remove(nums[i])
                j += 1
                i += 1
            else:
                return True
        return False

if __name__=='__main__':
    s = Solution()
    nums = [1,1]
    k = 1
    tt = s.containsNearbyDuplicate(nums,k)
    print (tt)
