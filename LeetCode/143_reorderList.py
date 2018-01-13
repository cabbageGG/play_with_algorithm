#-*- coding: utf-8 -*-
'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        pre,slow,fast = None,head,head
        while fast and fast.next:
            pre,slow,fast = slow,slow.next,fast.next.next
        pre.next = None
        slow = self.reverse(slow)
        cur1,cur2 = head,slow
        while cur1.next:
            cur1.next,cur2.next,cur1,cur2 = cur2,cur1.next,cur1.next,cur2.next
        cur1.next = cur2
        return head

    def reverse(self,head):
        pre = None
        cur = head
        while cur:
            cur.next,pre,cur = pre,cur,cur.next
        return pre

if __name__ == '__main__':
    s = Solution()
    L = [1,2,3,4]
    head = ListNode(L[0])
    cur = head
    for v in L[1:]:
        newNode = ListNode(v)
        cur.next = newNode
        cur = cur.next
    tem = head
    input = []
    while tem:
        input.append(tem.val)
        tem = tem.next
    print("input: %s" % input)
    s.reorderList(head)
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print("output: %s" % res)
