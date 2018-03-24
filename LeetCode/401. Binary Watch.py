#-*- coding: utf-8 -*-
'''
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
'''

class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        #求出最大的时间和最小的时间。返回位于中间的所有时间的列表
        #错误的思路。。。。要考虑实际组合，需要穷举法，分别小时和分钟，再组合！！              
        res = []
        for n in range(num+1):   
            list_h = [str(i) for i in range(12) if bin(i)[2:].count('1') == n]
            list_m = [str(i) for i in range(60) if bin(i)[2:].count('1') == num-n]
            list_m = ['0'+ i if int(i) < 10 else i for i in list_m]
            res += [i+':'+j for i in list_h for j in list_m]
        return res