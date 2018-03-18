#-*- coding: utf-8 -*-
'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
'''

class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """ 
        #利用二进制来计算，实现加法，得到新的二进制，再转化为数字
        #bin(num) int(str,2)
        a = list(bin(a)[2:])
        b = list(bin(b)[2:])
        def add(s,t,flag):
            if flag == 0:
                if s == '0' and t == '0':
                    return '0',0
                elif (s == '1' and t == '0') or (s == '0' and t == '1'):
                    return '1',0
                else:
                    return '0',1
            else:
                if s == '0' and t == '0':
                    return '1',0
                elif (s == '1' and t == '0') or (s == '0' and t == '1'):
                    return '0',1
                else:
                    return '1',1
        flag = 0
        if len(a) >= len(b):
            for i in range(-1,-len(b)-1,-1):
                a[i],flag = add(a[i],b[i],flag)
            for i in range(-len(b),-len(a)-1,-1):
                a[i],flag = add(a[i],'0',flag)
            return int(''.join(a),2)
        else:
            for i in range(-1,-len(a)-1,-1):
                b[i],flag = add(a[i],b[i],flag)
            for i in range(-len(a),-len(b)-1,-1):
                b[i],flag = add(b[i],'0',flag)
            return int(''.join(b),2)
        
a = Solution()
c = a.getSum(1,2)
print(c)