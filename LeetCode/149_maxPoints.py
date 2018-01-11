#-*- coding: utf-8 -*-

'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
'''

# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        #确定两个点是否在一条直线上，可通过斜率来判断。
        #所以，字典存储某个点下，其他所有点对他的斜率为key，斜率的频次为值。代表有多少个点在同一条直线上。

        #这是错误的思路！！！因为一条直线还由与y轴的截距有关。  
        #但好像，题目本身存在这样的漏洞，使得这种解法是对的。

        #需注意：斜率需要保存为分数形式。
        from fractions import Fraction
        max_points = 1
        l = len(points)
        if l<1:
            return 0
        for i in range(l-1):
            d = {'INF':1} #注意有可能有相同的点，斜率还可能是无穷大
            same = 0
            for j in range(i+1,l):
                #注：这里不能使用points[i] == points[j]，这两个实例对象本身不相等。只是他们拥有相同的属性！！！
                if points[i].x == points[j].x and points[i].y == points[j].y : 
                    same += 1
                    # continue  #不要使用continue，很耗时间！！！
                elif points[i].x == points[j].x:
                    d['INF'] += 1
                else:
                    k = Fraction((points[i].y - points[j].y),(points[i].x-points[j].x))
                    d[k] = d.get(k,1) + 1
            max_points = max(max_points,max(d.values())+same)
        return max_points  

if __name__ == '__main__':
    s = Solution()
    # [[0,0],[94911151,94911150],[94911152,94911151]]
    # [[0,0],[1921151,1921150],[1921152,1921151]]
    ss = [Point(0,0),Point(1921151,1921150),Point(1921152,1921151)]
    tt = s.maxPoints(ss)
    print (tt)