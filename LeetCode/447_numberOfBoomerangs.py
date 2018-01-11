#-*- coding: utf-8 -*-

'''
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).
'''

class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        #思路：以i节点为核心，则存储所有其他节点到i的距离数。
        #某一个距离L下的数目n，有方法数=n*(n-1)，即对应其它点到i有相同距离L的个数。
        count = 0
        for point1 in points:
            d = {}
            for point2 in points:
                if point2 != point1:
                    dis = (point1[0] - point2[0])*(point1[0] - point2[0]) + (point1[1] - point2[1])*(point1[1] - point2[1])
                    d[dis] = d.get(dis,0) + 1
            for key,value in d:
                count += value * (value-1)    
        return count