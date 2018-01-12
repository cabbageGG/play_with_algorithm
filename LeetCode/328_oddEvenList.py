#-*- coding: utf-8 -*-

'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ..
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        head2 = head.next
        pre1 = head
        pre2 = head2
        if not pre2:
            return head
        cur = pre2.next
        head.next = None  #注意每次考察节点，需要切断与前一个节点的连接！！！！
        head2.next = None
        #从第三个节点开始考察
        count = 2
        while cur:
            count += 1
            if count%2:
                pre1.next = cur
                pre1 = cur
            else:
                pre2.next = cur
                pre2 = cur
            tem = cur.next
            cur.next = None #注意每次考察节点，需要切断与前一个节点的连接！！！！
            cur = tem
        pre1.next = head2 
        return head