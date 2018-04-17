#-*- coding: utf-8 -*-
'''
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将这个元素所在的行和列都置零。

你有没有使用额外的空间?
使用 O(mn) 的空间不是一个好的解决方案。
使用 O(m + n) 的空间有所改善，但仍不是最好的解决方案。
你能设计一个使用恒定空间的解决方案吗？
'''

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        i_set = set()
        j_set = set()
        if not matrix:
            return 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    i_set.add(i)
                    j_set.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in i_set:
                    matrix[i][j] = 0
                elif j in j_set:
                    matrix[i][j] = 0
        
                    