#-*- coding: utf-8 -*-

'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        #注意：链表的结束时需要将两个链表重新拼接起来
        count,pre,cur = 0,None,head
        pre_mNode,mNode,nNode,next_nNode = None,None,None,None
        while cur:
            count += 1
            if count == m-1:
                pre_mNode = cur
            if count == m:
                mNode = cur
            if count == n:
                nNode = cur
            if count > n:
                next_nNode = cur
                break
                
            if count >= m:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            else:
                cur = cur.next
        if pre_mNode:
            pre_mNode.next,mNode.next = nNode,next_nNode
        else:
            head,mNode.next = nNode,next_nNode
        return head

if __name__ == '__main__':
    # s = Solution()
    # nums1 = [0]
    # nums2 = [1]
    # tt = s.merge(nums1,0,nums2,1)
    # print (nums1,tt)
