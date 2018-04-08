#-*- coding: utf-8 -*-
# '''
# 给出正整数 n，生成正方形矩阵，矩阵元素为 1 到 n2 ，元素按顺时针顺序螺旋排列。

# 例如，
# 给定正整数 n = 3，

# 应返回如下矩阵：

# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

# '''

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for i in range(n)] for j in range(n)]
        #螺旋构造，只有四种走法：j++, i++, j--, i--,
        num = i = j = 0
        statu = "right"
        while num < n ** 2:
            num += 1
            res[i][j] = num
            l = 2
            while l:
                if statu == "right":
                    if j == n-1 or res[i][j+1] > 0:
                        statu = "down"
                    else:
                        j += 1
                        break
                if statu == "down":
                    if i == n-1 or res[i+1][j] > 0:
                        statu = "left"
                    else:
                        i += 1
                        break
                if statu == 'left':
                    if j == 0 or res[i][j-1] > 0:
                        statu = "up"
                    else:
                        j -= 1
                        break
                if statu == 'up':
                    if i == 0 or res[i-1][j] > 0:
                        statu = "right"
                    else:
                        i -= 1
                        break
                l -= 1
        return res

if __name__ == "__main__":            
    a = Solution()
    print(a.generateMatrix(3))
