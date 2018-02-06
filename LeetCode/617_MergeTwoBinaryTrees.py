#-*- coding: utf-8 -*-
'''
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
Note: The merging process must start from the root nodes of both trees.
'''

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        head = t1
        self.merge(t1,t2)
        return head
    
    def merge(self,t1,t2):
        if t1 and t2:
            t1.val += t2.val
            if not t1.left:
                t1.left = t2.left
                t2.left = None
            if not t1.right:
                t1.right = t2.right
                t2.right = None
            self.merge(t1.left,t2.left)
            self.merge(t1.right,t2.right)
        else:
            return



        