#-*- coding: utf-8 -*-
'''
Sort a linked list using insertion sort.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #基本思想：由于链表不能反向查找比较，也不能构成双层循环。所以，肯定得重新构建一个链表，用于存储最终的有序链表。
        #每次从现有的链表中取一个元素，遍历新链表找到插入位置，并将元素插入。
        if not head:
            return head
        cur = head.next
        head.next = None
        while cur:
            tem = head
            pre = None
            while tem:
                if cur.val < tem.val:
                    #插入当前节点cur
                    if not pre: #往头部追加
                        head = cur
                    else:#
                        pre.next = cur
                    tem_cur_next = cur.next
                    cur.next = tem
                    break
                else:
                    #移动新链表
                    pre = tem
                    tem = tem.next
            #正常循环退出，则将值插入新链表尾部
            if not tem:
                pre.next = cur
                tem_cur_next = cur.next
                cur.next = None
            #外层循环的下次迭代
            cur = tem_cur_next
        return head


            
                

        