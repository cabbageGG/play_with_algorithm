#-*- coding: utf-8 -*-
'''
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pre = None
        cur = head
        while cur:
            if cur.val == val:
                if not pre:
                    head = cur.next
                else:
                    pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return head
        