#-*- coding: utf-8 -*-
'''
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    #     res = []
    #     self.get_res(root,res)
    #     return res

    # def get_res(self,root,res):
    #     if root:
    #         self.get_res(root.left,res)
    #         self.get_res(root.right,res)
    #         res.append(root.val)
    
        #新思路：使用栈来存储一个tuple，tuple元素包括，节点和是否需要打印的flag
        stack = []
        res =[]
        if not root:
            return res
        stack.append(('go',root))
        while stack:
            p = stack.pop()
            if p[0] == 'print':
                res.append(p[1].val)
            else:
                stack.append(('print',p[1]))
                if p[1].right:
                    stack.append(('go',p[1].right))
                if p[1].left:
                    stack.append(('go',p[1].left))
        return res
