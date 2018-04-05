#-*- coding: utf-8 -*-
'''
给定一个元素都是正整数的数组A ，正整数 L 以及 R (L <= R)。

求连续、非空且其中最大元素满足大于等于L 小于等于R的子数组个数。

例如 :
输入: 
A = [2, 1, 4, 3]
L = 2
R = 3
输出: 3
解释: 满足条件的子数组: [2], [2, 1], [3].
注意:

L, R  和 A[i] 都是整数，范围在 [0, 10^9]。
数组 A 的长度范围在[1, 50000]。
'''

class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        #思路：一定要敢于尝试，推导出递推逻辑。
        #比如：这里的，每增加一个元素时，应该怎么计算这个元素导致的符合条件的子数组！！！！
        res, dp = 0, 0
        prev = -1
        for i in range(len(A)):
            if A[i] < L and i > 0:
                res += dp
            if A[i] > R:
                dp = 0
                prev = i
            if L <= A[i] <= R:
                dp = i - prev
                res += dp
        return res

a = Solution()
print(a.numSubarrayBoundedMax([2,1,2,2],2,3))


        