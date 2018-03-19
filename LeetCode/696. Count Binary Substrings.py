#-*- coding: utf-8 -*-
'''
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
'''
class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # #遍历一遍字符串，只找连续的子串从start索引开始，先计数某一个，在计数另一个，两次相等则满足条件。然后从end位置继续循环。
        # num0,num1,res = 0,0,0
        # flag = False #判断是否比较计数，并重置
        # #两种情况先计数0，或先计数1
        # for i in s:
        #     if flag0 and falg1 and flag:
        #         if num0 == num1 and num0 > 0:
        #             res += 1
        #         num0,num1 = 0,0
        #     if i == '0':
        #         if flag1 and flag0:
        #             flag00 = True
        #             if num0 == num1 and num0 > 0:
        #                 res += 1
        #             num0,num1 = 0,0
        #         flag0 = True
        #         num0 += 1
        #     else
        #         if not flag0:
        #             flag1 = True
        #         else
        #             end1 = True
        #         num1 += 1


        #First, I count the number of 1 or 0 grouped consecutively.
        #For example “0110001111” will be [1, 2, 3, 4].

        #Second, for any possible substrings with 1 and 0 grouped consecutively, the number of valid substring will be the minimum number of         #0 and 1.
        #For example “0001111”, will be min(3, 4) = 3, ("01", "0011", "000111")

        s = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split()))
        return sum(min(a, b) for a, b in zip(s, s[1:]))

        #总结：自己思路是对的，计数寻找0,1的个数，相等则代表符合。
        #      但是怎么个计数，有待思考，上面正确的是直接划分group，来计数更合理！！！！