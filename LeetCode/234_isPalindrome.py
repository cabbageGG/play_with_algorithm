#-*- coding: utf-8 -*-
'''
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        pre,slow,fast = None,head,head
        while fast and fast.next:
            pre,slow,fast = slow,slow.next,fast.next.next
        pre.next = None
        slow = self.reverse(slow)
        while slow and head:
            if slow.val != head.val:
                return False
            slow,head = slow.next,head.next
        return True
    def reverse(self,head):
        pre,cur = None,head
        while cur:
            cur.next,pre,cur = pre,cur,cur.next
        return pre
