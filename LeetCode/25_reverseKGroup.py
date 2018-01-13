#-*- coding: utf-8 -*-

'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        tem = head
        count = 0
        dmmNode = ListNode(0)
        dmmNode.next = tem
        pre = dmmNode
        tem_head,tem_tail = None,None
        while tem:
            tem_next = tem.next
            if count % k == 0:
                tem_head = tem
            if count % k == k - 1:
                tem_tail = tem
                tem_next = tem.next
                tem.next = None
            if tem_head and tem_tail:
                newHead,newTail = self.reverse(tem_head)
                pre.next = newHead
                newTail.next = tem_next
                pre = newTail
                tem_head,tem_tail = None,None
            tem = tem_next
            count += 1 
        if tem_head:
            pre.next = tem_head
        return dmmNode.next

    def reverse(self,head):
        #初始化
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre,head

if __name__ == '__main__':
    s = Solution()
    L = [1,2]
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
    r = s.reverseKGroup(head,3)
    res = []
    while r:
        res.append(r.val)
        r = r.next
    print("output: %s" % res)