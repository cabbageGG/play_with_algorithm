#-*- coding: utf-8 -*-
'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #分析：只需将1和3替换，3和5替换，这样依次替换下去，如果没有可替换的，则再末尾加上。
        if not head or not head.next:
            return head
        tem = head
        head = head.next
        tem.next = None
        cur = head.next
        pre = head
        while cur:
            #replace nodes
            pre.next = tem
            tem.next = cur.next

            tem_pre = tem
            tem_cur = tem.next

            tem = cur
            tem.next = None

            pre = tem_pre
            cur = tem_cur
            
            if not cur:
                break
            else:
                pre = cur
                cur = cur.next
        pre.next = tem
        return head
        