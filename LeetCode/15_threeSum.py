#-*- coding: utf-8 -*-

'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # #基本思路：借助twoSum来降维处理。需注意：解的去重！！！
        # #1、set无法存储list元素，故不能使用set去重
        # #2、这使用大list的查找去重，需先对list的子元素小list进行排序，然后查找小list是否在大list中。
        # l = len(nums)
        # res = []
        # if l<3:
        #     return res
        # for i in range(l):
        #     rets = self.twoSum(nums[i+1:],-nums[i])
        #     for ret in rets:
        #         s = [nums[i],ret[0],ret[1]]
        #         s.sort()  #不能链式写，由于sort()不返回。
        #         if s not in res:
        #             res.append(s)
        #     i += 1
        # return res

        
        #特别注意去重，一定要在循环的过程中，自动去重，不能单独去重。
        #单独去重，虽然只会增加系数级别的时间复杂度，但是会导致超时。
        
        #所以，思路一，超时！！！！！！

        #second 思考：
        #由于复杂度必然超过nlogn，故可以采用先排序后，再进行求解。会降低难度，而不会增加时间复杂度！！！
        nums.sort()
        l = len(nums)
        res = []
        if l<3:
            return res
        for i in range(l-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            rets = self.twoOrderSum(nums[i+1:],-nums[i])
            for ret in rets:
                s = [nums[i],ret[0],ret[1]]
                res.append(s)
            i += 1
        return res

    def twoOrderSum(self,nums,target):
        #解决思路：
        #使用两个指针从前后分别开始寻找。
        l = len(nums)
        i = 0
        j = l-1
        ret = []
        while i<j:
            sum = nums[i] + nums[j]
            if sum == target:
                ret.append([nums[i],nums[j]])
                while i+1<j and nums[i] == nums[i+1]:
                    i += 1
                while i<j-1 and nums[j] == nums[j-1]:
                    j -= 1 
                i += 1
            elif sum > target:
                j -= 1
            else:
                i += 1
        return ret
    
    def twoSum(self,nums,target):
        #解决索引存储时，会覆盖的问题。
        #1、一开始不直接把所有的元素放入字典。
        #2、而是，每次判断一个，就放入一个，即使有覆盖前面的元素也无影响。
        #3、因为字典里面的元素只需要有一个即可。另一个是我们每次判断的元素。
        l = len(nums)
        d = {}
        res2 = []
        for i in range(l):
            complement = target - nums[i]
            if complement in d:
                res2.append([nums[d[complement]],nums[i]])
            else:
                d[nums[i]] = i
        return res2

if __name__ == '__main__':
    s = Solution()
    ss = [-1,0,1,2,-1,-4]
    ss = [0,0,0,0]
    tt = s.threeSum(ss)
    print (tt)