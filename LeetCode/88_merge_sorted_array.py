#-*- coding: utf-8 -*-

'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
'''

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        #将nums1数组中的数，向后移动n位。此时nums1[n,m+n-1]。
        for i in range(m,0,-1):
            nums1[i-1+n] = nums1[i-1]
        #合并nums1和nums2元素。
        #k:表示nums1已存在元素的开始索引。nums1[n,m+n-1]
        #j:表示nums2已存在元素的开始索引。nums2[j,n-1]
        #i:表示nums1合并后的开始索引。nums1[i,m+n-1]
        i = n
        j = 0
        k = 0
        while j<n and i<m+n:
            if nums2[j] < nums1[i]:
                nums1[k] = nums2[j]
                j += 1
            else:
                nums1[k] = nums1[i]
                i += 1
            k += 1
        while j<n:
            nums1[k] = nums2[j]
            j += 1 
            k +=1  
                   

        
if __name__ == '__main__':
    s = Solution()
    nums1 = [0]
    nums2 = [1]
    tt = s.merge(nums1,0,nums2,1)
    print (nums1,tt)