#-*- coding: utf-8 -*-

'''
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #注意：不是相邻的是最小的！！！而是父节点与左儿子的最右节点或右儿子的最左节点。。
        #
        #  二分搜索树，千万要记得上述情况，特别容易忽略！！！！！！！！！！！！！！！
        #
        m = n = 0x7FFFFFFF
        if not root:
            return 0x7FFFFFFF
        if root.left:
            tem = root.left
            while tem.right:
                tem = tem.right
            m = root.val - tem.val
        if root.right:
            tem = root.right
            while tem.left:
                tem = tem.left
            n = tem.val - root.val
        return min(m,n,self.getMinimumDifference(root.left),self.getMinimumDifference(root.right))