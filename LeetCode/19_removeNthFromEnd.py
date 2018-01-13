#-*- coding: utf-8 -*-
'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        k1,k2 = head,head
        count = 0
        while k1 and count<=n-1:
            count += 1
            k1 = k1.next
        dmmNode = ListNode(0)
        dmmNode.next = head
        pre = dmmNode
        while k1:
            pre = k2
            k1 = k1.next
            k2 = k2.next
        pre.next = k2.next
        return dmmNode.next    

