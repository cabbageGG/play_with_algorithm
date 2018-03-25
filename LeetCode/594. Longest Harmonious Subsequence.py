#-*- coding: utf-8 -*-
'''
We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.


'''
class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #思路：这种问题肯定不可能o(n)解决，那么可以考虑先排序，这样问题就简化啦。
        if not nums:
            return 0
        nums.sort() 
        res = tem0 = tem1 = 0
        start_num = nums[0]
        for num in nums:
            if num - start_num == 0:
                tem0 += 1
            elif num -start_num == 1:
                tem1 += 1
            else:
                if tem1:
                    res = max(res,tem0+tem1)
                if num - start_num == 2 and tem1:
                    start_num += 1
                    tem0 = tem1
                    tem1 = 1
                else:
                    start_num = num
                    tem0 = 1
                    tem1 = 0
        if tem1:
            res = max(res,tem0+tem1)
        return res
                
        