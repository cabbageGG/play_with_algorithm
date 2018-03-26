#-*- coding: utf-8 -*-
'''
给定一个索引 k，返回帕斯卡三角形（杨辉三角）的第 k 行。

例如，给定 k = 3，

则返回 [1, 3, 3, 1]。
      1  
     1 1
   1  2  1
 1  3  3  1
注：

你可以优化你的算法到 O(k) 的空间复杂度吗？
'''
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        L = [1,1]
        while rowIndex > 1:
            L = [1] + [L[i]+L[i+1] for i in range(len(L)-1)] + [1]
            rowIndex -= 1
        return L
