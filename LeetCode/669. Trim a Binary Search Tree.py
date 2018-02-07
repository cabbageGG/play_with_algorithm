#-*- coding: utf-8 -*-
'''
Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:
Input: 
    1
   / \
  0   2

  L = 1
  R = 2

Output: 
    1
      \
       2
Example 2:
Input: 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output: 
      3
     / 
   2   
  /
 1
 '''

 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        #find new root
        #需要重新确定root
        #先找到大于等于L的节点，即为新的root节点

        #find L
        #在root的左子树中找，如果root.left < L则root.left = None。此时，已经修剪好。
        #（这种做法有问题，因为root.left的右子树是大于root.left的，可能是满足条件的！！！）
        #find R
        #在新的root节点下，在root的右子树里寻找，如果root.right > R则root.right = None.

        #思路改进
        #如果root.left < L，则需要找到正确的root.left。root.left = None 或者 是root.left的右子树中满足条件的root节点
        #根据这种思路，很显然需要使用递归的解法！！！
        if not root:
            return None
        if L > root.val:
            return self.trimBST(root.right,L,R)
        if R < root.val:
            return self.trimBST(root.left,L,R)
        root.left = self.trimBST(root.left,L,R)
        root.right = self.trimBST(root.right,L,R)
        return root