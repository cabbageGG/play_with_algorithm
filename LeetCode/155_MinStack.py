#-*- coding: utf-8 -*-
'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

#思路：让每个元素绑定一个在它之前(包括自己)的所有元素的最小值。
#      则栈的元素变成一个有两个元素的tuple。

class MinStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.stack.append((x,curMin))

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        self.stack.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][0]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.stack
    
    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        return None
# Your MinStack object will be instantiated and called as such:
x = ["MinStack","push","push","push","getMin","pop","top","getMin"]
obj = MinStack()
obj.push(x)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()