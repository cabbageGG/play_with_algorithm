#-*- coding: utf-8 -*-

'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
'''

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        d1 = Counter(s)
        d2 = {}
        #这里特别注意：当dict键值相同的时候回覆盖掉的之前的存储，由于这里的值是字符串，故采用直接在之前的值的后面追加！！！！
        for key in d1.keys():      
            if d1[key] not in d2:
                d2[d1[key]] = d1[key] * key
            else:
                d2[d1[key]] += d1[key] * key
        orderd_key = list(d2.keys())
        orderd_key.sort(reverse=True)  #注：这里不能连写.sort。要分两步！
        res = [d2[key] for key in orderd_key]
        return "".join(res)

if __name__ == '__main__':
    s = Solution()
    ss = 'tree'
    tt = s.frequencySort(ss)
    print (tt)