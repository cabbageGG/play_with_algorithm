#-*- coding: utf-8 -*-

'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        cur = head
        pre = None
        #move to the insert position; save the pre and the next
        while cur and cur.val < x:
            pre = cur
            cur = cur.next
        if not cur:
            return head
        next = cur

        #begin to find the small Node
        tem_pre = cur
        while cur:
            if cur.val < x:
                #delete cur ; insert cur between pre and next; pre = cur
                tem_pre.next = cur.next #delete
                
                if not pre:
                    head = cur
                else:
                    pre.next = cur  #insert
                cur.next = next
                pre = cur

                cur = tem_pre.next #find next small Node 
            else:
                tem_pre = cur
                cur = cur.next
        return head
            