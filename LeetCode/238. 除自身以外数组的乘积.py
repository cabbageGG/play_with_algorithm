#-*- coding: utf-8 -*-
'''
一个长度为 n 的整形数组nums，其中 n > 1，返回一个数组 output ，其中 output[i] 等于nums中除nums[i]以外所有元素的乘积。

不用除法 且在O(n)内解决这个问题。

例如，输入 [1,2,3,4]，返回 [24,12,8,6]。

进阶：
你可以在常数空间复杂度内解决这个问题吗？（注意：出于空间复杂度分析的目的，输出数组不被视为额外空间。）
'''

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #出于题目的条件，答案肯定是只能循环一遍，或者两遍。
        #所以，需要保存中间结果。我们可以把保存的结果存放在要输出的数组。
        #循环两遍的思路：先正向遍历，保存每个元素位置之前的所有元素的乘积，
        #              然后反向遍历，保存每个元素位置之后的所有元素的乘积。
        
        res = []
        p = 1
        for i in range(len(nums)):
            res.append(p)
            p = p * nums[i]
        p = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * p
            p = p * nums[i]
        return res