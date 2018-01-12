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
        while k<=lenght:
            #将链表分成长度为k的多个链表,分别排序后，重新连接为一条链表
            tem = head
            count = 0  #自己创建索引！！！！
            while tem:
                if count % (2*k):
                    l1 = tem #找到l1的头结点，同时断开与前面节点的连接。并保存前面的节点。pre
                if count:
                    #断开l1的尾节点
                    #同时找到l2的头结点
                    l2 = 1
                if count:
                    #断开l2的尾节点,存储尾节点的下一个节点 next
                    #merge(l1,l2)
                    #将新的链表的尾节点，接上前面保存的next节点。
                    #并将新的链表的头结点与开始保存的pre节点连接。
                    l1 =3 
                #继续循环
            pass

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


    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
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
        return head