#-*- coding: utf-8 -*-
'''
将包含 n 个元素的数组向右旋转 k 步。

例如，如果  n = 7 ,  k = 3，给定数组  [1,2,3,4,5,6,7]  ，向右旋转后的结果为 [5,6,7,1,2,3,4]。

注意:

尽可能找到更多的解决方案，这里最少有三种不同的方法解决这个问题。

[显示提示]

提示:

要求空间复杂度为 O(1)

关联的问题: 反转字符串中的单词 II
'''
'''
三步法
[1,2,3,4,5] k = 3 

[1,2,5,4,3] 后k位[len(nums)-k:]反转

[3,4,5,2,1] 前k位[:k]与后k位[len(nums)-k:]互换 #思路错误，整个数组从前到后全部互换！！

[3,4,5,1,2] 后L-k位[k:]反转


[1,2,3,4,5,6,7] k = 3

[1,2,3,4,7,6,5]

[5,6,7,4,3,2,1]

[5,6,7,1,2,3,4]

[-1,-100,3,99] k = 3

[-1,99,3,-100]

[-100,3,99,-1]


'''



class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 
        L = len(nums)
        k = k % L
        if k == 0:
            return
        #后k位[L-k:L-1]反转
        i,j = L-k,L-1
        while i<j:
            tem = nums[i]
            nums[i] = nums[j]
            nums[j] = tem
            i += 1
            j -= 1
        #整个数组[0,L-1]从前到后全部互换!!!!!!!!!!   
        i,j = 0,L-1
        while i < j:
            tem = nums[i]
            nums[i] = nums[j]
            nums[j] = tem
            i += 1
            j -= 1
        #后L-k位[k:L-1]反转
        i,j = k,L-1
        while i<j:
            tem = nums[i]
            nums[i] = nums[j]
            nums[j] = tem
            i += 1
            j -= 1 
        
            
        
        
a = [1,2,3,4]
