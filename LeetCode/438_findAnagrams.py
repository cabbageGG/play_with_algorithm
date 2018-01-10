#-*- coding: utf-8 -*-

'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
'''

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ret = []
        ls = len(s)
        lp = len(p)
        if ls < lp:
            return ret
        #核心点：判断两个相同长度的字符串是否是anagram。
        target_dict = {}
        for i in p:
            if i in target_dict:
                target_dict[i] = target_dict[i] + 1
            else:
                target_dict[i] = 1
        tem_dict = {}
        for i in s[0:lp-1]:
            if i in tem_dict:
                tem_dict[i] = tem_dict[i] + 1
            else:
                tem_dict[i] = 1
        i = lp-1
        while i < ls:
            if s[i] in tem_dict:
                tem_dict[s[i]] += 1
            else:
                tem_dict[s[i]] = 1
            if tem_dict == target_dict:
                ret.append(i-lp+1)
            if tem_dict[s[i-lp+1]] > 1:
                tem_dict[s[i-lp+1]] -= 1
            else:
                del tem_dict[s[i-lp+1]]
            i += 1
        return ret


    
if __name__ == '__main__':
    s = Solution()
    ss = "cbaebabacd" 
    pp = "abc"
    tt = s.findAnagrams(ss,pp)
    print (tt)