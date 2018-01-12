#-*- coding: utf-8 -*-

'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
       #注意:怎么删除链表节点
        if head == None:
            return []
        pre = head
        cur = head.next
        pre_value = pre.val
        while cur:
            if cur.val == pre_value:
                pre.next = cur.next
            else:
                pre_value = cur.val
                pre = cur
            cur = cur.next
        return head
