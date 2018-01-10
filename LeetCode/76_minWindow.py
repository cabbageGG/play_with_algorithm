#-*- coding: utf-8 -*-

'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
'''

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #滑动窗口法。
        minW = ""
        ls = len(s)
        lt = len(t)
        if ls < lt:
            return minW
        #核心点：使用字典来保存string的构成字符串统计，从而判断两个字符串是否构成包含关系。
        tem_dict = {} #辅助字典来存储，字符频次
        counter = 0   #辅助变量来存储，是否目标string的各个字符在字典中的总频次
        for i in t:
            if i in tem_dict:
                tem_dict[i] = tem_dict[i] + 1
            else:
                tem_dict[i] = 1
            counter += 1
        #滑动窗口法。
        #初始窗口大小为lt-1，即：初始窗口范围[0,lt-2]
        #遍历初始窗口，得到差值dict。
        for i in range(0,lt-1):#左开右闭。
            if s[i] in tem_dict:
                tem_dict[s[i]] -= 1
                if tem_dict[s[i]] >= 0:
                    counter -= 1
    
        i = lt - 1
        j = 0
        #i,j 索引，从i开始考察，直到符合条件，更新最小窗口，
        #并开始尝试减小窗口大小j--，看是否可以最小。再次遇到不符合，则停止j。重新开始移动i。
        while i < ls:
            if s[i] in tem_dict:
                tem_dict[s[i]] -= 1
                if tem_dict[s[i]] >= 0:
                    counter -= 1
            while True:
                if counter == 0:
                    #符合条件
                    if minW == '':
                        minW = s[j:i+1]
                    #查看此次最小窗口，是否需要更新
                    if len(s[j:i+1]) < len(minW):
                        minW = s[j:i+1]
                    #开始缩小窗口，抛出j元素
                    if s[j] in tem_dict:
                        tem_dict[s[j]] += 1
                        if tem_dict[s[j]] > 0:
                            counter += 1
                    j += 1
                else:
                    break
            i += 1
        return minW

if __name__ == '__main__':
    s = Solution()
    S = "ADOBECODEBANC"
    T = "ABC"
    tt = s.minWindow(S,T)
    print (tt)