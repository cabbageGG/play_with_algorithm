#-*- coding: utf-8 -*-
'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
'''

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        output = []
        row1 = 'qwertyuiopQWERTYUIOP'
        row2 = 'asdfghjklASDFGHJKL'
        row3 = 'zxcvbnmZXCVBNM'
        for word in words:
            flag = 0
            if word[0] in row1:
                row = row1
            elif word[0] in row2:
                row = row2
            else:
                row = row3
            for i in word:
                if i not in row:
                    flag = 1
                    break
            if not flag:
                output.append(word)
        return output
            