#-*- coding: utf-8 -*-
'''
给定一棵树的中序遍历与后序遍历，依据此构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 = [9,3,15,20,7]
后序遍历 = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return 
        root = TreeNode(postorder[-1])
        index = inorder.index(root.val)
        root.left = self.buildTree(inorder[:index],postorder[:index])
        root.right = self.buildTree(inorder[index+1:],postorder[index:len(postorder)-1])
        return root
        
        
