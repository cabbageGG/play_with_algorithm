#-*- coding: utf-8 -*-
'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        #将l2合并到l1中
        head = l1
        pre1 = None
        while l1 and l2:
            if l2.val < l1.val:
                #插入l2节点到l1中
                if not pre1:
                    head = l2
                else:
                    pre1.next = l2
                pre1 = l2   #注：这里不要忘记更新pre1指针
                tem = l2.next
                l2.next = l1
                l2 = tem
            else:
                pre1 = l1
                l1 = l1.next
        if not l1:
            pre1.next = l2
        return head