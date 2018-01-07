#-*- coding: utf-8 -*-

# author: li yangjin

import time, random
from test__all_sort import quick_sort

"""
借助快速排序的partition函数，与递归思想解决求解数组中第k大的数。
算法思想：
1、partition函数，将数组的第一个元素放置在数组正确的排序位置，并返回该位置的索引。
2、将partition函数返回的索引对应的元素与目标元素比较，若大，则要寻找的元素在索引的右边；若小，则要寻找的元素在索引的左边。
3、对目标元素，进行递归的partition操作查找，知道返回的索引对应的元素等于目标元素，退出。
 
算法复杂度：O(n)
注：n + n/2 + n/4 ....+0 极限等于 2n。所以算法复杂度为O(n)
"""

def genRandomArr(length,min,max):
    return [random.randint(min,max) for i in range(length)]

def get_max_k(list,k):
    l = len(list)
    if k > l or k < 1: #错误输入
        return -1
    return _get_max_k(list,0,l-1,k-1)

def _get_max_k(list,l,r,k):
    if l >= r:
        return l
    index = partition(list,l,r)
    if index == k:
        return list[index]
    elif index > k:
        return _get_max_k(list,l,index,k)
    else:
        return _get_max_k(list,index+1,r,k)

def partition(list,l,r):
    #随机下
    a = random.randint(l,r)
    if a != l:
        list[l],list[a] = list[a],list[l]
    v = list[l]
    # list[l+1,j] < v and list[j+1,i) > v
    j = l
    i = l + 1
    while True:
        if list[i] < v:
            list[i],list[j+1] = list[j+1],list[i]
            j = j + 1
        i = i + 1
        if i>=r:
            break
    list[l],list[j] = list[j],list[l]
    return j

if __name__ == '__main__':
    n = 10000
    a = genRandomArr(n, 0, n)
    a1 = a[:] #这里是数组的拷贝
    a2 = a[:]
    k = n//2

    start_time = time.time()
    a.sort()
    end_time = time.time()
    cost_time = end_time - start_time
    print("第%s大的数是：%s" % (k,a[k-1]))
    print("系统库排序:" + str(cost_time))

    start_time = time.time()
    quick_sort(a1)
    end_time = time.time()
    cost_time = end_time - start_time
    print("第%s大的数是：%s" % (k,a1[k-1]))
    print("quick_sort:" + str(cost_time))

    start_time = time.time()
    num = get_max_k(a2,k)
    end_time = time.time()
    cost_time = end_time - start_time
    print("第%s大的数是：%s" % (k,num))
    print("get_max_k:" + str(cost_time))
