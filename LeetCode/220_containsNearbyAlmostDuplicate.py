#-*- coding: utf-8 -*-
'''
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
'''

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        #新的思路：针对于新参数t，可以使用n//t将，数组中的值以t归一化,取整。
        #         则查找是否有n-t<n<n+t的数, 变成查找值为[n-1,n,n+1]里的人一个，且两个值的索引差小于k，即满足条件。
        #         可以使用OrderedDict()来存储这样的数，key为数组的归一化值，作为查找关键字。
        #         两个值的索引差k，可以使用维持OrderedDict的大小为k来保证。
        if k<=0 or t<0:
            return False
        from collections import OrderedDict
        d = OrderedDict()
        for n in nums:
            key = n if not t else n // t  #检查t是否为0
            for m in (d.get(key-1),d.get(key),d.get(key+1)):
                if m is not None and abs(n-m) <= t:
                    return True
            if len(d)==k:
                d.popitem(False) #传入False，表示抛出第一个元素，而不是最后一个元素 
            d[key] = n
        return False
    
if __name__ == '__main__':
    from collections import OrderedDict
    d = OrderedDict()
