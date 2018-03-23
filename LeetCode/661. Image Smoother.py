#-*- coding: utf-8 -*-
'''
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].

'''
class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if not M:
            return [[]]
        row = len(M)
        col = len(M[0])
        #res = [[0] * col ] * row  #注意：这里共用内存啦，不行的！！！！！
        res = []
        for i in range(row):
            tem = []
            for j in range(col):
                #获取周围8个元素的值M[i-1][j-1],M[i-1][j],M[i-1][j+1]
                #                  M[i][j-1],  M[i][j], M[i][j+1]
                #                 M[i+1][j-1],M[i+1][j],M[i+1][j+1]
                nums = 1
                sum = M[i][j]
                if i-1 >=0 and j-1>=0:
                    sum += M[i-1][j-1] 
                    nums += 1
                if i-1 >=0 and j>=0:
                    sum += M[i-1][j] 
                    nums += 1 
                if i-1 >=0 and j+1 <= col-1:
                    sum += M[i-1][j+1] 
                    nums += 1
                if i >=0 and j-1 >= 0:
                    sum += M[i][j-1] 
                    nums += 1                  
                if i >=0 and j+1 <= col-1:
                    sum += M[i][j+1] 
                    nums += 1
                if i+1 <= row-1 and j-1 >= 0:
                    sum += M[i+1][j-1] 
                    nums += 1 
                if i+1 <= row-1 and j >= 0:
                    sum += M[i+1][j] 
                    nums += 1
                if i+1 <= row-1 and j+1 <= col-1:
                    sum += M[i+1][j+1] 
                    nums += 1
                tem.append(sum//nums)
            res.append(tem)
        return res
