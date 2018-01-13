#-*- coding: utf-8 -*-
'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''

class Solution:
    def __init__(self):
        self.operators = {
            '+':lambda y,x:x+y,
            '-':lambda y,x:x-y,
            '*':lambda y,x:x*y,
            '/':lambda y,x:int(x/y)
        }

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        #一开始没搞懂这个题目的意思。借用栈来存放数据，遇到操作符，取出顶上两个数据进行操作！！！
        if not tokens:
            return
        stack = []
        for token in tokens:
            if token in self.operators.keys():
                stack.append(self.operators[token](stack.pop(),stack.pop()))
            else:
                stack.append(int(token))
        return stack[0]

if __name__ == '__main__':
    s = Solution()
    ss = ['1','2','+','1']
    tt = s.evalRPN(ss)
    print (tt)
