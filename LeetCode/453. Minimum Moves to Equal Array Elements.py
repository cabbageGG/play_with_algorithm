#-*- coding: utf-8 -*-
'''
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
'''

class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #  大神解析，很犀利。需要想明白，要想得到最小的次数，每次minNum必须属于参与加法运算！！！ 
        # let’s define sum as the sum of all the numbers, before any moves; minNum as the min number int the list; n is the length of the list;

        # After, say m moves, we get all the numbers as x , and we will get the following equation

        # sum + m * (n - 1) = x * n
        # and actually,

        # x = minNum + m
        # and finally, we will get

        # sum - minNum * n = m
        # So, it is clear and easy now.

        #经分析，这是一个数学问题
        #所有元素与最小元素的差的和，就是最终结果
        return sum(nums) - min(nums) * len(nums)