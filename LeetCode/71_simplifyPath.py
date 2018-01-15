#-*- coding: utf-8 -*-
'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
'''
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        #思路：1、先排除不符合要求的文件夹路劲，比如：'./', '//'等。
        #     2、 解决'../'回退问题。
        #     根据以上思路，需要想到将字符串以'/'分割！！！！！！ 
        places = path.split('/')
        stack = []
        for p in places:
            if p == '..':
                if stack:
                    stack.pop()
            else:
                if p and p != '.':
                    stack.append(p)
        return '/'+'/'.join(stack)