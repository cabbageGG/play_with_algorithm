#-*- coding: utf-8 -*-
'''
一个长度为 n + 1 的整形数组，其中的数字都在 1 到 n 之间，包括 1 和 n ，可知至少有一个重复的数字存在。假设只有一个数字重复，找出这个重复的数字。

注意：

不能更改数组内容（假设数组是只读的）。
只能使用恒定的额外空间，即要求空间复杂度是 O(1) 。
时间复杂度小于 O(n2)
数组中只有一个数字重复，但它可能不止一次重复出现
'''
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]