#-*- coding: utf-8 -*-
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s = 0 #是否有进位，只能为0或1
        head = l1
        while l1 and l2:
            value = l1.val + l2.val + s
            if value >= 10:
                value = value - 10
                s = 1
            else:
                s = 0
            l1.val = value
            pre1 = l1 #用于保存l1最后一个节点
            l1 = l1.next
            pre2 = l2 #用于保存l2最后一个节点
            l2 = l2.next
        if not l1: #如果链表2比1长，则把2的后半部分，拼接在1后面
            l1 = pre2.next
            pre1.next = l1
        while l1:
            value = l1.val + s
            if value >= 10:
                value = value - 10
                s = 1
            else:
                s = 0
            l1.val = value
            pre1 = l1  #用于保存l1最后一个节点
            l1 = l1.next
        if s:
            newNode = ListNode(s)
            pre1.next = newNode
        return head






