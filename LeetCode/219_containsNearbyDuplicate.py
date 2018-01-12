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
        s = set()  #注意：这里必须使用set()，虽然list也可当做查找表，但是由于底层实现不同。list查找复杂度大于set，会超时。
        if k==0:
            return False
        #建立初始查找表，将前k-1个元素放入查找表，若有重复则直接返回True。
        #初始查找表长度为k-1，且没有重复元素
        while j<k and j<l:
            if nums[j] not in s:
                s.add(nums[j])
                j += 1
            else:
                return True
        #运行到这里，说明此时j=k。则从k索引开始考察，若nums[k]在set[0,k-1]中，则返回True；
        #否则，将nums[k]追加在set，同时抛出set头部元素，维持set大小为k。
        while j<l:
            if nums[j] not in s:
                s.add(nums[j])  
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
