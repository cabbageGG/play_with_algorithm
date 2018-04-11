#-*- coding: utf-8 -*-
'''
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

示例 1:

输入: [2,2,3,4]
输出: 3
解释:
有效的组合是: 
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3
注意:

数组长度不超过1000。
数组里整数的范围为 [0, 1000]。
'''
class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #n**3 方法超时，很显然题目应该是需要n**2的解法。而我们的有效判别条件是两个较小的数的和，大于最大的数。
        # 则，可以想到将寻找两个较小的数，改为寻找两个较小的数的和，这样就从n**2将到n啦！！！！
        
        # n**3 解法
        
        # res = 0
        # L = len(nums)
        # if L < 3:
        #     return res
        # nums.sort()      
        # for i in range(L-2):
        #     if nums[i] <= 0:
        #         continue
        #     for j in range(i+1,L-1):
        #         for k in range(j+1,L):
        #             if nums[i] + nums[j] > nums[k]:
        #                 res += 1
        #             else:
        #                 break
        # return res
        
        #n**2解法
        res = 0
        L = len(nums)
        if L < 3:
            return res
        nums.sort(reverse=True)
        for i in range(L-2):
            j,k = i + 1,L-1
            while j < k:
                if nums[k] > 0 and nums[j] + nums[k] > nums[i]:
                    res += k - j
                    j += 1
                else:
                    k -= 1
        return res
        
