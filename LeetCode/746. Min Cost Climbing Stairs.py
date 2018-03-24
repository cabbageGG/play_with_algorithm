#-*- coding: utf-8 -*-
'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].

'''
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        #递归解法超时！！
        # if len(cost) == 2:
        #     return min(cost[0],cost[1])
        # if len(cost) == 1:
        #     return 
        # return min(cost[0]+self.minCostClimbingStairs(cost[1:]),cost[1]+self.minCostClimbingStairs(cost[2:]))
        
        #最后一步有重复计算，可以使用cache！！！！！！！！！！！！！！！！
        #
        cache = dict()
        def min_f(cost,i): #从取了第i个元素之后，的最小值。
            if not cost or i >= len(cost):
                return 0
            if i in cache.keys():
                return cache[i]
            cache[i] = min(cost[i] + min_f(cost,i+1),cost[i] + min_f(cost,i+2))
            return cache[i]
        return min(min_f(cost,0),min_f(cost,1))
                
        
        #解法升级，从后往前，遍历一次。每两个元素比较一下，取其中较小的。然后从被取的那个元素的下两个元素进行比较！！
        # res = 0
        # i = -1
        # while i-1 >= -len(cost):
        #     if cost[i] < cost[i-1]:
        #         res += cost[i]
        #         i -= 1
        #     else:
        #         res += cost[i-1]
        #         i -= 2
        # return res
    
        #还是有问题。。。。[0,2,2,1] -> 3 ; 应该是2
        #正确解法应该是，从前往后，以第一个开始的最小值，与以第二个开始的最小值，比较，输出较小的。
        # res1 = cost[0]
        # i = 1
        # while i+1 <= len(cost)-1:
        #     if cost[i] < cost[i+1]:
        #         res1 += cost[i]
        #         i += 1
        #     else:
        #         res1 += cost[i+1]
        #         i += 2
        # res2 = cost[1]
        # i = 2
        # while i+1 <= len(cost)-1:
        #     if cost[i] < cost[i+1]:
        #         res2 += cost[i]
        #         i += 1
        #     else:
        #         res2 += cost[i+1]
        #         i += 2
        # return min(res1,res2)
        # #继续错误：[0,1,2,2]
        # #在此升级，只一遍循环，多加一层判断
        # res = 0
        # i = 0
        # while i+1 <= len(cost)-1:
        #     if cost[i] < cost[i+1]:

        #循环有解法吗？？？
        #肯定有的。利用一个历史变量保存上一次最小的值。
        #解释：
        #现有两种方案，旧方案和新方案。
        #当来一个新的数时，我们需要基于现有的方案，提取出新方案。
        #得到新方案的思路是：比较两种方案，以较好的方案+新的数成为新的方案，同时备用上次新方案为旧方案，以防止误操作！
        #这里的误操作是指，当来的新的数是最后一个数时。这时需要回退一个版本的方案。
        
        old_method,new_method = cost[0],cost[1] #初始化两种方案。
        for c in cost[2:]:
             old_method,new_method = new_method,min(old_method,new_method) + c
        new_method = min(old_method,new_method) #是否回退一个版本的方案
        return new_method