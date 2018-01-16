#-*- coding: utf-8 -*-
'''
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    #     res = []
    #     self.get_res(root,res)
    #     return res
    
    # def get_res(self,root,res):
    #     if root:
    #         res.append(root.val)
    #         self.get_res(root.left,res)
    #         self.get_res(root.right,res)

        # # 思路：借助栈来实现，迭代前序遍历二叉树。
        # #       栈存储的是访问过的且有左孩子的二叉树节点，一旦出现其左孩子即没有左孩子，
        # #       也没有右孩子，则需要取出栈顶的元素，访问其右孩子。
        # stack = []
        # res = []
        # while root:
        #     res.append(root.val)
        #     if root.left:
        #         stack.append(root)
        #         root = root.left
        #     elif root.right:
        #         root = root.right
        #     else:
        #         isHas = False
        #         while stack:
        #             root = stack.pop()
        #             if root.right:
        #                 isHas = True
        #                 root = root.right
        #                 break
        #         if not isHas:
        #             break
        # return res

        #新思路：使用栈来存储一个tuple，tuple元素包括，节点和是否需要打印的flag
        stack = []
        res = []
        if root == None:
            return res
        stack.append(('go',root))
        while stack:
            p = stack.pop()
            if p[0] == 'print':
                res.append(p[1].val)
            else:
                if p[1].right:
                    stack.append(('go',p[1].right))
                if p[1].left:
                    stack.append(('go',p[1].left))
                stack.append(('print',p[1]))
        return res
            


            
