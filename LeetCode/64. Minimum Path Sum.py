#-*- coding: utf-8 -*-
'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
[[1,3,1],
 [1,5,1],
 [4,2,1]]
Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.
'''
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #递归试试, 超时！！
        # if not grid:
        #     return 0
        # rows = len(grid)
        # cols = len(grid[0])
        # def f(i,j):
        #     if i == rows -1 and j == cols - 1:
        #         return grid[i][j]
        #     if i == rows -1:
        #         return grid[i][j] + f(i,j+1)
        #     if j == cols -1:
        #         return grid[i][j] + f(i+1,j)
        #     return min(f(i+1,j),f(i,j+1)) + grid[i][j]
        # return f(0,0)
        
        #使用空间，加循环。dp问题
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0 for i in range(cols)] for j in range(rows)]#初始化dp
        dp[0][0] = grid[0][0]
        for i in range(1,rows):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for j in range(1,cols):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        for i in range(1,rows):
            for j in range(1,cols):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        return dp[rows-1][cols-1]
        
        
        

# a = Solution()
# input = [[1,3,1],[1,5,1],[4,2,1]]
# a.minPathSum(input)
a = [[0 if col!=0 else 8 for col in range(3)] for row in range(4)]
print(a)
a[0] = [1,2,3]
print(a)