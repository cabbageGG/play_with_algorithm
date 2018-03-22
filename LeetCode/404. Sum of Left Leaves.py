#-*- coding: utf-8 -*-
'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #终止条件的判断很关键
        if not root:
            return 0
        elif root.left:
            if not root.left.left and not root.left.right:
                if root.right:
                    return root.left.val + self.sumOfLeftLeaves(root.right)
                else:
                    return root.left.val                
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        