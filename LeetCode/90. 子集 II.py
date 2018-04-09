#-*- coding: utf-8 -*-
'''
给定一个可能包含重复整数的列表，返回所有可能的子集（幂集）。

注意事项：解决方案集不能包含重复的子集。

例如，如果 nums = [1,2,2]，答案为：

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        import itertools
        nums.sort()
        for x in range(len(nums)):
            for i in itertools.combinations(nums,x+1):
                res.add(i)
        return [list(i) for i in res]+[[]]

a = Solution()
print(a.subsetsWithDup([1,2,2]))
