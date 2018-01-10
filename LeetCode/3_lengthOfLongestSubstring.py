#-*- coding: utf-8 -*-

'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #使用两个指针的滑块法
        #合法子串[i,j),则 tem = s[i:j]。从j索引判断增加一个字符s[j]的情况，若没有重复，则j++；
        #否则，有重复，从i++开始减少子串，直到将重复元素去掉！！！
        i,j =0,0
        l = len(s)
        tem = s[i:j]
        maxLength = 0
        while i<=j and j<l:
            if s[j] not in tem:
                j += 1
            else:
                i += 1
            tem = s[i:j] #注：这里是左开右闭，不包含j索引元素
            maxLength = max(maxLength,len(tem))
        return maxLength

if __name__ == '__main__':
    s = Solution()
    ss = "abcabcbb"
    tt = s.lengthOfLongestSubstring(ss)
    print (tt)

            