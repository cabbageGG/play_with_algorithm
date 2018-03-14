#-*- coding: utf-8 -*-
'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        #思路：层序遍历
        #利用列表来做缓存，实现层序遍历
        #遍历每一层，将每一层的元素的儿子存放到一个列表中，得到新的一层。
        Nodes = []
        tem = []
        tem.append(root)
        while tem:
            Nodes.append([i.val for i in tem])
            tem1 = []
            for i in tem:
                if i.left:
                    tem1.append(i.left)
                if i.right:
                    tem1.append(i.right)
            tem = tem1.copy()
        return [sum(i)/len(i) for i in Nodes]

    

        

            