#-*- coding: utf-8 -*-
'''
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
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
    #         res.append(root.val)
    #         self.get_res(root.right,res)

        # #思路：和前序遍历一样的，迭代逻辑。不同的是，打印节点值的时机不一样。
        # #     前序的是，访问一个节点，就打印这个节点。而中序，则是访问一个节点，
        # #     这个节点没有左孩子就打印，且接着打印栈顶的元素。
        # stack = []
        # res = []
        # while root:
        #     if root.left:
        #         stack.append(root)
        #         root = root.left
        #     elif root.right:
        #         res.append(root.val)
        #         root = root.right
        #     else:
        #         res.append(root.val)
        #         isHas = False
        #         while stack:
        #             root = stack.pop()
        #             res.append(root.val)
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
                stack.append(('print',p[1]))
                if p[1].left:
                    stack.append(('go',p[1].left))
        return res