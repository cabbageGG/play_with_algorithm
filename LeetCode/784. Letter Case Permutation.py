#-*- coding: utf-8 -*-
'''
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length at most 12.
S will consist only of letters or digits.
'''

class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        #求字符串所有的排列组合，通过变大小写。
        #f(ab) = [ab,Ab,aB,AB] = [a,A] * [b,B] = af(b) + Af(b)
        #a = 'A'
        #b = ['b','B']
        #af(b) = [a+i for i in b]

        # #先将字母的索引提取出来,在将字母放在一个单独的列表中，为下面进行排列处理。
        index = [i for i in range(len(S)) if S[i].isalpha()]
        s = [S[i].lower() for i in index]
        #现在需要求所有s的组合
        #寻找排列的子串
        def f(s):
            if not s:
                return [""]
            a = s[0]
            b = s[1:]
            return [a+i for i in f(b)] + [a.upper()+i for i in f(b)] 
        
        def g(s,S):
            tem = list(S)
            for i in range(len(s)):
                tem[index[i]] = s[i]
            return ''.join(tem)

        ss = f(s)
        #将列表还原成字符串
        res = []
        for s in ss:
            res.append(g(s,S))
        return res

if __name__ == "__main__":
    # a = Solution()
    # res = a.letterCasePermutation("a1b2")
    # print(res)
    S = "1w2e3Q"
    L = [[i.lower(), i.upper()] if i.isalpha() else i for i in S]
    print(L)
    import itertools
    print([''.join(i) for i in itertools.product(*L)])