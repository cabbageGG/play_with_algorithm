#-*- coding: utf-8 -*-

# author: li yangjin

import time, random

"""
归并求解逆序对
1、一个数组的逆序对 = 将这个数组一分为二后两个数组自身的逆序对之和 + 这两个数组各取一个元素可以组成的逆序对
2、前面一部分相当于是递归求解，后一部分相当于两个数组合并求解。
3、对于后一部分的求解，由于是对两个数组，各取一个数组合求解逆序对。
   如果这两个数组各自排好序了，那就很方便的统计这两个数组可以组成的逆序对啦。
   于是，可以利用归并排序，在排序的过程中顺便统计逆序对的数目。  （这里理解很关键）
"""

def genRandomArr(length,min,max):
    return [random.randint(min,max) for i in range(length)]

def get_reverse_count_by_merge(list):
    count = 0
    l = len(list)
    count = _get_reverse_count_by_merge(list,0,l-1)
    return count

def _get_reverse_count_by_merge(list,l,r):
    if (l >= r):
        return 0 
    m = (l + r) // 2
    count1 = _get_reverse_count_by_merge(list,l,m)
    count2 = _get_reverse_count_by_merge(list,m+1,r)
    count3 = merge_count(list,l,m,r)
    return count1+count2+count3

def merge_count(list,l,m,r):
    count = 0
    #归并排序，并统计两个数组可以构成的逆序对
    temp = []
    i = l
    j = m + 1
    while i<=m and j<=r:
        if list[i] < list[j]:
            temp.append(list[i])
            i = i + 1
            # count = count + (j-m-1) #list[i]<list[j], j后面的都可以跟i构成顺序对，包含j，这里暂不统计
        else:
            temp.append(list[j])
            j = j + 1
            count = count + (m-i+1) #list[i]>=list[j]，i后面的都可以跟j构成逆序对，包含i  
    while i<=m: 
        temp.append(list[i])
        i = i + 1   
    while j<=r:
        temp.append(list[j])
        j = j + 1  
    for k in range(l,r+1):
        list[k] = temp[k-l]   
    return count

def get_reverse_count(list):
    count = 0
    l = len(list)
    for i in range(l-1):
        for j in range(i+1,l):
            if list[i] >= list[j]:
                count = count + 1
    return count

if __name__ == '__main__':
    n = 1000
    a = genRandomArr(n, 0, n)
    a1 = a[:] #这里是数组的拷贝
    a2 = a[:]

    count = 0
    start_time = time.time()
    count = get_reverse_count(a1)
    end_time = time.time()
    cost_time = end_time - start_time
    print("逆序对数量：%s" % count)
    print ("get_reverse_count耗时:"+str(cost_time))

    count = 0
    start_time = time.time()
    count = get_reverse_count_by_merge(a2)
    end_time = time.time()
    cost_time = end_time - start_time
    print("逆序对数量：%s" % count)
    print ("get_reverse_count_by_merge耗时:"+str(cost_time))

    # 逆序对数量：249005
    # get_reverse_count耗时:1.74000000954
    # 逆序对数量：249005
    # get_reverse_count_by_merge耗时:0.149000167847