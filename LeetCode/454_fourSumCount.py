#-*- coding: utf-8 -*-
'''
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -2^28 to 2^28 - 1 and the result is guaranteed to be at most 2^31 - 1.
'''

class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        d = {}
        for i in range(len(A)):
            for j in range(len(B)):
                tem = A[i] + B[j]
                if tem in d:
                    d[tem] += 1
                else:
                    d[tem] = 1
        count = 0
        for i in range(len(C)):
            for j in range(len(D)):
                target = -(C[i] + D[j])
                if target in d:
                    count += d[target]
        return count 