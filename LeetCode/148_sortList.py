#-*- coding: utf-8 -*-
'''
Sort a linked list in O(n log n) time using constant space complexity.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        lenght = 0
        while cur:
            lenght += 1
            cur = cur.next
        k = 1

        #构造虚拟节点
        dmmyNode = ListNode(0)
        dmmyNode.next = head

        while k<=lenght:
            #将链表分成长度为k的多个链表,合并排序后，重新连接为一条链表
            #具体为：每次截取两个连续的长度为k的链表，合并排序后，放回原链表，
            #       继续取下两个长度为k的链表，重复操作，直到结尾。
            tem = head
            pre = dmmyNode
            head1,last1,head2,last2 = None,None,None,None
            count = 0  #自己创建索引！！！！
            while tem:
                if count % k == 0: #找到一个头结点
                    if not head1:
                        head1 = tem
                    else:
                        head2 = tem
                if count % k == k - 1:#找到一个尾节点
                    if not last1:
                        last1 = tem
                        tem_next = last1.next
                        last1.next = None #尾部断开原链表
                    else:
                        last2 = tem
                        tem_next = last2.next
                        last2.next = None #尾部断开原链表
                if head1 and head2:
                    newHead,newLast = self.mergeTwoLists(head1,last1,head2,last2)
                    pre.next = newHead
                    newLast.next = tem_next
                    pre = newLast
                    head1,head2 = None,None
                    last1,last2 = None,None
                tem = tem_next
            if head1:
                pre.next = head1
            

#         #自底向上的归并排序
# def merge_sort2(list):
#     length = len(list)
#     k = 1
#     while k<=length:
#         for i in range(0,length,2*k):
#             l = i
#             r = min(length-1,i+2*k-1)
#             m = min(length-1,i + k -1)
#             merge(list,l,m,r)
#         k = k * 2


    def mergeTwoLists(self, l1,last1,l2,last2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2,last2
        if not l2:
            return l1,last1
        #将l2合并到l1中
        head = l1
        pre1 = None
        while l1 and l2:
            if l2.val < l1.val:
                #插入l2节点到l1中
                if not pre1:
                    head = l2
                else:
                    pre1.next = l2
                pre1 = l2   #注：这里不要忘记更新pre1指针
                tem = l2.next
                l2.next = l1
                l2 = tem
            else:
                pre1 = l1
                l1 = l1.next
        if not l1:
            pre1.next = l2
        #遍历寻找最后一个节点
        while pre1:
            last = pre1
            pre1 = pre1.next
        return head,last