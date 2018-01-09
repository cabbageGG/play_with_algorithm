#-*- coding: utf-8 -*-

'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        i = 0
        j = l - 1
        while i<j:
            while i<j and not s[i].isalnum():
                i += 1
            while i<j and not s[j].isalnum():
                j -= 1
            if s[i].upper() == s[j].upper():
                i += 1
                j -= 1
            else:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    ss = "a.b,."
    ss[0].isalnum()
    tt = s.isPalindrome(ss)
    print (tt)

