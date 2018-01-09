#-*- coding: utf-8 -*-

'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
'''
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        import re
        pattern = re.compile(r'(?i)[aioue]')  #注：这里(?i)表示忽略大小写
        s = list(s)   #注：这里需要转换为list，因为后面字符串不支持s[i],s[j] = s[j],s[i]这个索引修改操作。
        l = len(s)
        i,j = 0,l-1
        while i<j:
            while i<j and not re.match(pattern,s[i]):
                i += 1
            while i<j and not re.match(pattern,s[j]):
                j -= 1
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
        return "".join(s)


    def reverseVowels1(self, s):
        import re
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s) #re.sub(pattern,repl,string) 按正则表达式替换。
        #不懂这个m的作用？？

    
if __name__ == '__main__':
    s = Solution()
    ss = "hEilleo"
    tt = s.reverseVowels1(ss)
    print (tt)
        

