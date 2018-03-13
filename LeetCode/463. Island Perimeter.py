#-*- coding: utf-8 -*-

'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
'''

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #思路： L = 1的数目 * 4 - 两两相邻1的对数 * 2
        #直接一行行遍历。将每一行的1的位置记录下来。从而计算相邻1的个数。
        # 即，每一行里相邻1的个数，该行与上一行相邻1的个数。
        #每一行里相邻1的个数:使用标记符号来统计相邻1的个数
        #该行与上一行相邻1的个数：保存相邻两行1的索引位置，求交集。
        nums = 0  
        tem = set() #保存每行有1的索引位置
        tem1 = set() #保存上一行1的索引位置
        for i in range(len(grid)):
            n = 0
            flag = False
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    tem.add(j)
                    if flag:
                        n += 1
                    flag = True
                else:
                    flag = False
            if len(tem) > 0:
                tem1 = tem.intersection(tem1)
                nums = nums + 4 * len(tem) - 2 * n - len(tem1) *2
                tem1 = tem.copy()
                tem.clear()
        return nums

