#-*- coding: utf-8 -*-

'''
Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        #两个指针i,j 从前往后搜索。i,j的和小于s，则j++增加元素，大于s，就尝试i++减少元素，以得到最小的长度。
        l = len(nums)
        if l < 1:
            return 0
        i,j = 0,0
        sum = nums[0]
        minlength = l+1
        while i<=j and j<l:
            if sum >= s:
                minlength = min(j - i + 1,minlength)
                sum -= nums[i]
                i += 1
            else:
                j += 1
                if j<l:
                    sum += nums[j]
        if minlength == l+1:
            return 0
        return minlength

[2,3,1,2,4,3]
if __name__ == '__main__':
    s = Solution()
    ss = [2,3,1,2,4,3]
    tt = s.minSubArrayLen(7,ss)
    print (tt)
                


