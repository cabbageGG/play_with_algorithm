#-*- coding: utf-8 -*-

'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # #暴力解法：height[i,j]
        # maxArea = 0
        # l = len(height)
        # for i in range(l):
        #     for j in range(i+1,l):
        #         maxArea = max(min(height[i],height[j]) * (j-i),maxArea)
        # return maxArea

        #双指针索引法，从最开始和结尾，想中间逼近。那边小则那边开始想中间移动。
        l = len(height)
        i,j = 0,l-1
        maxArea = 0
        while i<j:
            maxArea = max(min(height[i],height[j]) * (j-i),maxArea)
            if height[i]<height[j]:
                i += 1
            else:
                j -= 1
        return maxArea






if __name__ == '__main__':
    s = Solution()
    ss = [1,1]
    tt = s.maxArea(ss)
    print (tt)