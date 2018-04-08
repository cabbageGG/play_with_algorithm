#-*- coding: utf-8 -*-
'''
给定一个 n × n 的二维矩阵表示一个图像。

将图像旋转 90 度（顺时针）。

注意：

你必须在原矩阵中旋转图像，请不要使用另一个矩阵来旋转图像。

例 1:

给出的输入矩阵 = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

旋转输入矩阵，使其变为 :
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
 

例 2:

给出的输入矩阵 =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

旋转输入矩阵，使其变为 :
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return 
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i < j:
                    tem = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = tem
        return 