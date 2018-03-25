#-*- coding: utf-8 -*-
'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.


Example 1:

Input: 2
Output:  2
Explanation:  There are two ways to climb to the top.

1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output:  3
Explanation:  There are three ways to climb to the top.

1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #递归超时。。
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # return self.climbStairs(n-1)+self.climbStairs(n-2)
    
        #改进递归，使用cache   通过啦，哈哈。
        # cache = {}
        # def f(n):
        #     if n == 1:
        #         return 1
        #     if n == 2:
        #         return 2
        #     if n in cache.keys():
        #         return cache[n]
        #     cache[n] = f(n-1) + f(n-2)
        #     return cache[n]
        # return f(n)
        
    
        #改成循环。递推公式为。f(n) = f(n-1) + f(n-2)
        f,f1,f2 =0,1,2
        for i in range(3,n+1):
            f = f1 + f2
            f1,f2 = f2,f
        if n == 1:
            return f1
        if n == 2:
            return f2
        return f
        
        
        