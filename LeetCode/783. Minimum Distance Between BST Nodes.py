#-*- coding: utf-8 -*-
'''
Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
Note:

The size of the BST will be between 2 and 100.
The BST is always valid, each node's value is an integer, and each node's value is different.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
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
        return min(m,n,self.minDiffInBST(root.left),self.minDiffInBST(root.right))