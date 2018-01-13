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

        while k<lenght:
            #测试每次处理的结果，用于debug
            tem = head
            test = []
            while tem:
                test.append(tem.val)
                tem = tem.next
            print("k=%d,link_in=%s" % (k,test))
            #将链表分成长度为k的多个链表,合并排序后，重新连接为一条链表
            #具体为：每次截取两个连续的长度为k的链表，合并排序后，放回原链表，
            #       继续取下两个长度为k的链表，重复操作，直到结尾。
            tem = head
            #构造虚拟节点
            dmmyNode = ListNode(0)
            dmmyNode.next = head
            pre = dmmyNode
            head1,last1,head2,last2 = None,None,None,None
            count = 0  #自己创建索引！！！！
            while tem:
                tem_next = tem.next  #这个很关键，保证每次循环必需有正确的tem_next
                if count % k == 0: #找到一个头结点
                    if not head1:
                        head1 = tem                       
                    else:
                        head2 = tem
                if count % k == k - 1:#找到一个尾节点
                    if not last1:
                        last1 = tem
                        tem_next = tem.next
                        last1.next = None #尾部断开原链表
                    else:
                        last2 = tem
                        tem_next = tem.next
                        last2.next = None #尾部断开原链表
                if not tem_next or (head1 and last1 and head2 and last2):
                    newHead,newLast = self.mergeTwoLists(head1,head2)
                    pre.next = newHead
                    newLast.next = tem_next
                    pre = newLast
                    head1,head2 = None,None
                    last1,last2 = None,None            
                tem = tem_next
                #索引从零开始，这里索引加1
                count += 1
            #删除虚拟节点
            head = dmmyNode.next
            del dmmyNode
            #测试每次处理的结果，用于debug
            tem = head
            test = []
            while tem:
                test.append(tem.val)
                tem = tem.next
            print("k=%d,link_out=%s" % (k,test))
            #递归k
            k = k * 2
        return head
            
    def mergeTwoLists(self,l1,l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            cur = l2
            while cur:
                last = cur
                cur = cur.next
            return l2,last
        if not l2:
            cur = l1
            while cur:
                last = cur
                cur = cur.next
            return l1,last
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

if __name__ == '__main__':
    s = Solution()
    L = [4,3,2,1]
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
    r = s.sortList(head)
    res = []
    while r:
        res.append(r.val)
        r = r.next
    print("output: %s" % res)


#TODO:优化代码！！！