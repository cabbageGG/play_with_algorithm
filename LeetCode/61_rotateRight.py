#-*- coding: utf-8 -*-
'''
Given a list, rotate the list to the right by k places, where k is non-negative.

Example:

Given 1->2->3->4->5->NULL and k = 2,

return 4->5->1->2->3->NULL.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        k = k % length
        
        if k == 0:
            return head
        k1,k2 = head,head
        count = 0 
        while k1 and count<=k-1:
            count += 1
            k1 = k1.next
        dmmNode = ListNode(0)
        dmmNode.next = head
        pre1 = pre2 = dmmNode
        while k1:
            pre1,k1,pre2,k2 = k1,k1.next,k2,k2.next
        pre1.next,head,pre2.next = head,k2,None
        return head

