#-*- coding: utf-8 -*-
'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
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
        #思路：将链表遍历完，转换为数字，然后相加。再将相加后的和转化为链表输出。
        value1,value2 = 0,0
        while l1:
            value1 = l1.val + value1 * 10
            l1 = l1.next
        while l2:
            value2 = l2.val + value2 * 10
            l2 = l2.next
        value = value1 + value2
        strs = str(value)
        head = ListNode(int(strs[0]))
        cur = head
        for s in strs[1:]:
            newNode = ListNode(int(s))
            cur.next = newNode
            cur = cur.next
        return head