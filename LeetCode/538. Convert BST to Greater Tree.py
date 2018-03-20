#-*- coding: utf-8 -*-

'''
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #转化为中序遍历的列表
        L = []
        def f(node):
            if not node:
                return 
            f(node.left)
            L.append(node.val)
            f(node.right)
        f(root)
        S = [sum(L[i:]) for i in range(len(L))]
        S.reverse()
        def g(node):
            if not node:
                return
            g(node.left)
            node.val = S.pop()
            g(node.right)
        g(root)
        return root