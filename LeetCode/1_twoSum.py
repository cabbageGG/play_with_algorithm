#-*- coding: utf-8 -*-

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # l = len(nums)
        # for i in range(l-1):
        #     if target-nums[i] in nums:
        #         for j in range(i+1,l):
        #             if nums[j] == target-nums[i]:
        #                 return [i,j]


        #解决索引存储时，会覆盖的问题。
        #1、一开始不直接把所有的元素放入字典。
        #2、而是，每次判断一个，就放入一个，即使有覆盖前面的元素也无影响。
        #3、因为字典里面的元素只需要有一个即可。另一个是我们每次判断的元素。
        l = len(nums)
        d = {}
        for i in range(l):
            complement = target - nums[i]
            if complement in d:
                return [d[complement],i]
            else:
                d[nums[i]] = i
        

if __name__ == '__main__':
    s = Solution()
    ss = [11, 2, 2, 7, 11, 15]
    tt = s.twoSum(ss,9)
    print (tt)
