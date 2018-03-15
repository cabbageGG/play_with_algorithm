#-*- coding: utf-8 -*-
'''
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''

class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #思路：只要是4的倍数，我后手就能保证每次消耗4个。
        if n % 4 <= 3 and n % 4 != 0:
            return True
        else:
            return False