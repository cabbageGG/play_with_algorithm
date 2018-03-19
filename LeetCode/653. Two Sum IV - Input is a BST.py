#-*- coding: utf-8 -*-
'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
'''
class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        #中序遍历，搞成列表。two pointer方法
        L = []
        def f(node):
            if not node:
                return
            f(node.left)
            L.append(node.val)
            f(node.right)
            
        f(root)
        i,j = 0,len(L)-1
        while i < j:
            if L[i] + L[j] == k:
                return True
            elif L[i] + L[j] > k:
                j -= 1
            else:
                i += 1
        return False
            