#-*- coding: utf-8 -*-

'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = len(nums)
        #思路：使用快排的将数组分成一大一小的左右两个数组。
        #将返回的index与目标index比较，确定下次递归在哪个数组中查找
        #第k大，对应的索引为l-k
        target = l - k
        return self.get_max_k(nums,0,l-1,target)

    def get_max_k(self,nums,l,r,target):
        if l>=r:
            return nums[l]
        index = self.partition(nums,l,r)
        if index == target:
            return nums[index]
        elif index < target:
            l = index + 1
            return self.get_max_k(nums,l,r,target)
        else:
            r = index -1 
            return self.get_max_k(nums,l,r,target)

    def partition(self,nums,l,r):
        import random
        a = random.randint(l,r)
        # print ('a:',a)
        if a != l:
            list[l],list[a] = list[a],list[l]
        v = nums[l]
        #nums[l+1,i]<v  nums[i+1,k)=v   nums[j,r]>v
        i = l 
        k = l + 1
        j = r + 1
        while k<j:
            if nums[k] == v:
                k += 1
            elif nums[k] > v:
                nums[k],nums[j-1] = nums[j-1],nums[k]
                j -= 1
            else:
                nums[k],nums[i+1] = nums[i+1],nums[k]
                i += 1
                k += 1
        nums[l],nums[i] = nums[i],nums[l]
        return i

if __name__=='__main__':
    s = Solution()
    nums = [-1,-1]
    k = 2
    tt = s.findKthLargest(nums,k)
    print (tt)
            


