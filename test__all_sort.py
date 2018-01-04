#-*- coding: utf-8 -*-

# author: li yangjin
import time, random
"""
排序算法稳定性：对于相等的元素，在排序后，原来靠前的元素依然靠前。相等元素的相对位置没有发生变化。

选择排序思想：
1、从[i+1,n)里找最小值的索引。
2、最小值与i进行交换。

插入排序思想
1、将第i个元素，依次相邻比较,若比前一个元素小，则交换,继续与前一个比较; 否则当前在适当位置，退出循环。


冒泡排序思想
1、从最后开始，依次比较相邻的两个元素，如果第一个元素小于第二个元素，则交换。直到将最小的元素放在最前面。
2、改进：依次比较相邻元素，如果未发生交换，则说明已排好序。然后，上次交换的位置，之前的元素肯定也排好序了。

希尔排序思想（插入排序升级版---分组插入排序）
1、将元素序列以相隔为div进行分组，对每一组进行插入排序。 
2、增量每次减少一半，当增量为1时，最后一遍插入排序后，则说明已排好。

归并排序思想
1、将数组递归分解，比如：一分为二，二分为四，最终变成一个个元素。
2、逆向合并两个数组，且使之有序。需要借助一个新的空间来存放元素。

快速排序思想
1、划分数组，将数组中第一个元素放置在合适的位置，让数组变成在小于这个值和大于这个值的两个数组。
2、递归操作，让子数组仍然进行第一步的划分。

3路快速排序思想
1、多加一个中间层，即有一个大于v，小于v，还有一个等于v的区间，组成三个部分。
2、等于v的部分相当于排好序，不用管。递归解决剩余的小于和大于v的数组。

堆排序思想
1、堆有两个操作，一个是shiftUp，一个是shiftDown。
   shiftUp用于当尾部有一个新元素时，维持最大堆的性质，将新元素shiftUp到合适的位置。
   shiftDown用于当最大堆的最大元素被取走，会用最后一个元素来填补1号位置，
            但此时就不满足最大堆的性质，需要shiftDown这个1号位元素到合适位置。
            (此外，当一个新的数组时，可以通过count/2号位置开始shiftDown，直到1号位，实现最大堆创建。)
2、首先，创建一个最大堆，将1号位元素与最后元素互换。然后在前n-1个元素中，对1号元素进行shiftDown操作，使得前n-1个元素保持最大堆。
3、重复2操作，直到只剩下一个元素。

算法实用性扩展
1、不定类型数组
2、不定类型比较方式

算法测试
1、测试用例随机生成，更有实际不同算法比较价值
2、验证函数，测试结果是够正确
"""

#        a(0)
#     b(1)     c(2)
#   d(3)
# 第一个不是叶子节点的位置是3//2 即(count - 1) // 2
#

def heap_sort(list):
    l = len(list)
    #构建最大堆
    index = (l-1) // 2
    while index>=0:
        shift_down(list,l-1,index)
        index = index - 1
    #循环取出最大值，并维持剩下元素的最大堆性质
    while l > 1:
        list[0],list[l-1] = list[l-1],list[0]
        #剩余l-1个元素进行shift_down操作
        shift_down(list,l-2,0)
        l = l - 1

#传入list，list最后元素的索引r，以及需要shift_down元素的索引
def shift_down(list,r,index):
    while (2*index + 1) <= r:  #索引位置比较
        j = 2 * index + 1
        if j+1 <= r and list[j] < list[j+1]:
            j = j + 1
        if list[index] < list[j]:
            list[index],list[j] = list[j],list[index]
        index = j

def genRandomArr(length,min,max):
    return [random.randint(min,max) for i in range(length)]

def isSorted(list):
    for i in range(1, len(list)):
        if list[i-1] > list[i]:  #比较函数可以抽象出来
            return False
    return True

def select_sort(list):
    l = len(list)
    for i in range(l):
        minIndex = i
        for j in range(i+1,l):
            if list[j] < list[minIndex]:
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]

def insert_sort(list):
    l = len(list)
    for i in range(1,l):
        j = i
        #一次插入排序
        while j >= 1:
            if list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]
            else:
                break
            j = j - 1 

# def insert_sort_improve(list):
#     l = len(list)
#     for i in range(1,l):
#         e = list[i]
#         j = i 
#         #一个元素的插入过程
#         while j >= 1:
#             if e < list[j-1]:
#                 list[j] = list[j-1]
#             else:
#                 break
#             j = j - 1
#         list[j] = e

def shell_sort(list):
    l = len(list)
    div = l//2
    while div > 0:
        i = 0
        while i < div:  #这里i取一次值，代表一组相隔div的序列，需要进行插入排序
            j = i 
            while j < l:
                k = j
                #这里相当于一个元素的插入过程
                while k >= div:
                    if list[k] < list[k-div]:
                        list[k],list[k-div] = list[k-div],list[k]
                    else:
                        break
                    k = k - div
                j = j + div
            i = i + 1
        div = div//2

# def shell_sort_improve(list):
#     l = len(list)
#     div = l//2
#     while div > 0:
#         i = 0
#         while i < div:  #这里i取一次值，代表一组相隔div的序列，需要进行插入排序
#             j = i 
#             while j < l:
#                 e = list[j]
#                 k = j
#                 #这里相当于一个元素的插入过程
#                 while k >= div:
#                     if e < list[k-div]:
#                         list[k] = list[k-div]
#                     else:
#                         break
#                     k = k - div
#                 list[k] = e
#                 j = j + div
#             i = i + 1
#         div = div//2
    
def bubble_sort(list):
    l = len(list)
    for i in range(l):
        for j in range(l-1,i,-1):
            if list[j] < list[j-1]:
                list[j],list[j-1] = list[j-1],list[j]

# def bubble_sort_imporve(list):
#     l = len(list)
#     last_change_pos = 0
#     last_change_pos_tem = 0
#     for i in range(l):
#         last_change_pos = last_change_pos_tem
#         last_change_pos_tem = 0
#         for j in range(l-1,last_change_pos,-1):
#             if list[j] < list[j-1]:
#                 list[j],list[j-1] = list[j-1],list[j]
#                 last_change_pos_tem = j
#         if last_change_pos_tem is 0:
#             break        

def merge_sort(list):
    l = len(list)
    _merge_sort(list,0,l-1)

def _merge_sort(list,l,r):
    if r <= l:
        return   #终止条件不能忘记啦
    m = (r + l) // 2
    _merge_sort(list,l,m)
    _merge_sort(list,m+1,r)
    merge(list,l,m,r)

def merge(list,l,m,r):
    temp = []
    i = l
    j = m + 1
    while i<=m and j<=r:
        if list[i] < list[j]:
            temp.append(list[i])
            i = i + 1
        else:
            temp.append(list[j])
            j = j + 1
    while i <= m:
        temp.append(list[i])
        i = i + 1
    while j <= r:
        temp.append(list[j])
        j = j + 1
    
    for k in range(l,r+1):
        list[k] = temp[k-l]
    

def quick_sort(list):
    l = len(list)
    _quick_sort(list,0,l-1)

def _quick_sort(list,l,r):
    if r <= l:
        return 
    p = partition(list,l,r)
    _quick_sort(list,l,p)
    _quick_sort(list,p+1,r)

def partition(list,l,r):
    #inprove the quick_sort 当数组已然有序的时候。采用随机值，作为分界值。
    a = random.randint(l,r)
    list[l],list[a] = list[a],list[l]

    v = list[l]
    #list[l+1,j] < v  and  list[j+1,i) > v
    j = l
    i = l + 1
    while True:
        if list[i] < v:
            list[j+1],list[i] = list[i],list[j+1]
            j = j + 1
        i = i + 1
        if i > r:
            break
    list[j],list[l] = list[l],list[j]    
    return j

def quick_sort3(list):
    l = len(list)
    _quick_sort3(list,0,l-1)

def _quick_sort3(list,l,r):
    if r <= l:
        return

    #inprove the quick_sort 当数组已然有序的时候。采用随机值，作为分界值。
    a = random.randint(l,r)
    list[l],list[a] = list[a],list[l]

    v = list[l]
    #list[l+1,lt] < v and list[lt+1,i) = v and list[gt,r] > v
    lt = l
    i = lt + 1
    gt = r+1
    while True:
        if list[i] < v:
            list[lt+1],list[i] = list[i],list[lt+1]
            lt = lt + 1
            i = i + 1
        elif list[i] > v:
            list[i],list[gt-1] = list[gt-1],list[i]
            gt = gt - 1
        else:
            i = i + 1
        if i >= gt:
            break
    if l < lt:
        list[l],list[lt] = list[lt],list[l]
        lt = lt - 1

    _quick_sort3(list,l,lt)
    _quick_sort3(list,gt,r)

if __name__ == "__main__":
    n = 1000
    a = genRandomArr(n, 0, n)
    # a = list(range(900))  #这里递归栈不能到1000，否则会挂掉。
    a1 = a[:] #这里是数组的拷贝
    a2 = a[:]
    a3 = a[:]
    a4 = a[:]
    a5 = a[:]
    a6 = a[:]
    a7 = a[:]
    a8 = a[:]
    a9 = a[:]
    a10 = a[:]
    a11 = a[:]


    start_time = time.time()
    a.sort()
    end_time = time.time()
    cost_time = end_time - start_time
    print(isSorted(a))
    print ("系统库sort耗时:"+str(cost_time))

    start_time = time.time()
    select_sort(a1)
    end_time = time.time()
    cost_time = end_time - start_time
    print(isSorted(a1))
    print ("select_sort耗时:"+str(cost_time))

    start_time = time.time()
    insert_sort(a2)
    end_time = time.time()
    cost_time = end_time - start_time
    print(isSorted(a2))
    print("insert_sort耗时:" + str(cost_time))

    # start_time = time.time()
    # insert_sort_improve(a3)
    # end_time = time.time()
    # cost_time = end_time - start_time
    # print(isSorted(a3))
    # print("insert_sort_improve耗时:" + str(cost_time))

    start_time = time.time()
    bubble_sort(a4)
    end_time = time.time()
    cost_time = end_time - start_time
    print(isSorted(a4))
    print("bubble_sort耗时:" + str(cost_time))

    # start_time = time.time()
    # bubble_sort_imporve(a5)
    # end_time = time.time()
    # cost_time = end_time - start_time
    # print(isSorted(a5))
    # print("bubble_sort_imporve耗时:" + str(cost_time))

    start_time = time.time()
    shell_sort(a6)
    end_time = time.time()
    cost_time = end_time - start_time
    print(isSorted(a6))
    print("shell_sort耗时:" + str(cost_time))

    # start_time = time.time()
    # shell_sort_improve(a7)
    # end_time = time.time()
    # cost_time = end_time - start_time
    # print(isSorted(a7))
    # print("shell_sort_improve耗时:" + str(cost_time))

    start_time = time.time()
    merge_sort(a8)
    end_time = time.time()
    cost_time = end_time - start_time
    print(isSorted(a8))
    print("merge_sort耗时:" + str(cost_time))

    start_time = time.time()
    quick_sort(a9)
    end_time = time.time()
    cost_time = end_time - start_time
    print(isSorted(a9))
    print("quick_sort耗时:" + str(cost_time))

    start_time = time.time()
    quick_sort3(a10)
    end_time = time.time()
    cost_time = end_time - start_time
    print(isSorted(a10))
    print("quick_sort3耗时:" + str(cost_time))

    start_time = time.time()
    heap_sort(a11)
    end_time = time.time()
    cost_time = end_time - start_time
    print(isSorted(a11))
    print("heap_sort耗时:" + str(cost_time))