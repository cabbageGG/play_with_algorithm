#-*- coding: utf-8 -*-
'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #判断两个字符串是否是anagram，可以将字符串排序后，看是否相等！！！！
        #不一定要使用字典统计字符出现次数。
        d = {}
        for s in strs:
            sort_s = "".join(sorted(s))
            d[sort_s] = d.get(sort_s,[]) + [s]
        return d.values()    

if __name__ == '__main__':
    s = Solution()
    nums = ["eat","tea","tan","ate","nat","bat"]
    tt = s.groupAnagrams(nums)
    print (tt)
    
