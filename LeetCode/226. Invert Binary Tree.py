#-*- coding: utf-8 -*-
'''
Invert a binary tree.
     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def exchangeLR(node):
            if node:
                tem = node.left
                node.left = node.right
                node.right = tem
            else:
                return
            exchangeLR(node.left)
            exchangeLR(node.right)
        exchangeLR(root)
        return root