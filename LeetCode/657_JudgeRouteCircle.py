#-*- coding: utf-8 -*-
'''
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
'''

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        h = 0
        v = 0
        for i in moves:
            if i == 'U':
                v += 1
            elif i == 'D':
                v -= 1
            elif i == 'R':
                h += 1
            elif i == 'L':
                h -= 1
        if not h and not v:
            return True
        return False