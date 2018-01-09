#-*-coding:utf-8 -*-

'''
建立一个链表类
1、链表的节点内容：节点值和指向下一个节点的指针。
2、链表类的操作：初始化头结点，插入新的节点，获取下一个节点
'''

#链表数据结构定义
class LinkNode(object):
    __slots__=('value','nextNode')

    def __init__(self,value,nextNode=None):
        self.value = value
        self.nextNode = None
        if isinstance(nextNode,LinkNode) :
            self.nextNode = nextNode
# #初始化链表
# head = LinkNode(0)
# temp = head
# for i in range(1,5):
#     a = LinkNode(i)
#     temp.nextNode = a
#     temp = a

# #打印链表
# print (head.value)
# temp = head.nextNode
# while temp:
#     print (temp.value)
#     temp = temp.nextNode  

         

#定制链表类
class LinkList(object):
    def __init__(self,*args):
        self.head = None
        self.end = self.head
        for value in args:
            if self.end:
                self.end.nextNode = LinkNode(value)
                self.end = self.end.nextNode
            else:
                self.head = LinkNode(value)
                self.end = self.head
                
    def insert(self,node):
        if node:
            self.end.nextNode = node
            self.end = node
    
    def getNextNode(self,node=None):
        if node:
            return node.nextNode
        return self.head.nextNode

    def printNodes(self):
        if self.head:
            print (self.head.value)
            temp = self.head.nextNode
            while temp:
                print (temp.value)
                temp = temp.nextNode

if __name__ == '__main__':
    tt = LinkList(*range(5))
    print ('headNode：%s' % tt.head)
    tt.insert(LinkNode(999))
    tt.printNodes()
    # node = tt.getNextNode()
    # print node.value



