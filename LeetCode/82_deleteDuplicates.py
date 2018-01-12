#-*- coding: utf-8 -*-
'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        pre,cur1,cur2 = None,head,head.next
        same = 0
        while cur2:
            if cur2.val == cur1.val:
                cur2 = cur2.next   #这里运行完后，可能到末尾啦
                same = 1
            else:
                if same:
                    if not pre:
                        head = cur2
                    else:
                        pre.next = cur2
                    same = 0
                else:
                    pre = cur1
                cur1 = cur2
                cur2 = cur2.next
        if same:    #这里特别容易忘记判断！！！！
            if not pre:
                head = cur2
                same = 0
            else:
                pre.next = cur2
        return head


