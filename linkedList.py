#-*-coding:utf-8 -*-

'''
建立一个链表类
1、链表的节点内容：节点值和指向下一个节点的指针。
2、链表类的操作：初始化头结点，插入新的节点，获取下一个节点
'''

#链表数据结构定义
class LinkNode(object):
    __slots__=('value','next')

    def __init__(self,value,next=None):
        self.value = value
        self.next = None
        if isinstance(next,LinkNode) :
            self.next = next

#定制链表类
class LinkList(object):
    def __init__(self,*args):
        self.head = None
        self.tail = None
        self.length = 0
        for value in args:
            self.length += 1
            if self.tail:
                self.tail.next = LinkNode(value)
                self.tail = self.tail.next
            else:
                self.head = LinkNode(value)
                self.tail = self.head
                
    def insert(self,node):
        if node:
            self.length += 1
            self.tail.next = node
            self.tail = node
    
    def delete(self,node):
        if node.next:
            self.length -= 1
            node.value = node.next.value
            node.next = node.next.next
        else:
            print('the node is not exist or the node is tail node')
    
    def printNodes(self):
        s = '' 
        if self.head:
            s += str(self.head.value)
            temp = self.head.next
            while temp:
                s += '->'
                s += str(temp.value)
                temp = temp.next
        print (s)
    
    def reverse(self):
        pre,cur = None,self.head
        while cur:
            cur.next,pre,cur = pre,cur,cur.next
        self.head = pre

    def insertionSortList(self):
        #基本思想：由于链表不能反向查找比较，也不能构成双层循环。所以，肯定得重新构建一个链表，用于存储最终的有序链表。
        #每次从现有的链表中取一个元素，遍历新链表找到插入位置，并将元素插入。
        if not self.head:
            return None
        cur = self.head.next
        self.head.next = None
        while cur:
            pre,tem = None,self.head
            while tem:
                if cur.value < tem.value:
                    #插入当前节点cur
                    if not pre: 
                        self.head = cur
                    else:#
                        pre.next = cur
                    tem_cur_next = cur.next
                    cur.next = tem
                    break
                else:
                    pre,tem = tem,tem.next    #移动新链表
            if not tem: #正常循环退出，则将值插入新链表尾部
                pre.next,tem_cur_next,cur.next = cur,cur.next,None
            cur = tem_cur_next

    def sort(self):
        cur,k = self.head,1
        while k<self.length:
            #将链表分成长度为k的多个链表,合并排序后，重新连接为一条链表
            #具体为：每次截取两个连续的长度为k的链表，合并排序后，放回原链表，
            #       继续取下两个长度为k的链表，重复操作，直到结尾。
            tem = self.head
            #构造虚拟节点
            dmmyNode = LinkNode(0)
            dmmyNode.next = self.head
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
            self.head = dmmyNode.next
            del dmmyNode
            #递归k
            k = k * 2
            
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
            if l2.value < l1.value:
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
    L = [2,4,5,1,6,3]
    tt = LinkList(*L)
    print('初始链表:')
    tt.printNodes()
    tt.insert(LinkNode(999))
    print('插入节点999后链表:')
    tt.printNodes()
    tt.sort()
    print('排序后链表:')
    tt.printNodes()
    tt.reverse()
    print('反转后链表:')
    tt.printNodes()
    tt.delete(tt.head)
    print('删除头结点链表:')
    tt.printNodes()
    tt.insertionSortList()
    print('插入排序后链表:')
    tt.printNodes()



