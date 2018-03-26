#-*- coding: utf-8 -*-
'''
给定 numRows, 生成帕斯卡三角形的前 numRows 行。

例如, 给定 numRows = 5,

返回

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        res = [[1],[1,1]]
        L = [1,1]
        while numRows > 2:
            L = [1] + [L[i]+L[i+1] for i in range(len(L)-1)] + [1]
            numRows -= 1
            res.append(L)
        return res

