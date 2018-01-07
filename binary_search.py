#-*- coding: utf-8 -*-

# author: li yangjin

"""
二分查找法算法思想：
1、每次取数组中间元素，与目标元素进行比较。若大，则在左边数组，继续递归比较；若小，则在右边数组，继续递归比较。
2、若中间元素等于目标元素，即找到，返回该元素。当要查找的数组越界，说明整个数组没有目标元素，返回-1。

注意：二分查找法的基础是----查找有序数组。

扩展：
当有序数组的target元素有多个，即存在相等值的情况，需要返回第一个target元素的索引floor，和返回最后一个target元素的索引ceil
"""

def binary_search(list,target):
    l = len(list)
    if list[0] > target or list[l-1] < target:
        return -1
    return _binary_search(list,0,l-1,target)

#在闭区间list[l,r]里查找target元素。
def _binary_search(list,l,r,target):
    while l<=r:
        # mid = (l + r) // 2 #注：这里有可能出现溢出bug，最好使用下面的方式。虽然python的整数可以无限大，但还是规范写吧。
        mid = l + (r-l) // 2  
        if target == list[mid]:
            return mid
        elif target > list[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1 

def binary_search_recursion(list, target):
    l = len(list)
    if list[0] > target or list[l-1] < target:
        return -1
    return _binary_search_recursion(list, 0, l-1,target)

def _binary_search_recursion(list,l,r,target):
    if l>r:
        return -1
    mid = l + (r-l) //2 
    if target == list[mid]:
        return mid
    elif target > list[mid]:
        l = mid + 1
        return _binary_search_recursion(list,l,r,target)
    else:
        r = mid - 1
        return _binary_search_recursion(list,l,r,target)

def binary_search_floor_ceil(list,target):
    l = len(list)
    if list[0] > target:
        return None,0
    if list[l-1] < target:
        return l-1,None 
    return _binary_search_floor_ceil(list,0,l-1,target)

def _binary_search_floor_ceil(list,l,r,target):
    floor = l
    ceil = r
    while l<=r:
        mid = l + (r-l) // 2  
        if target == list[mid]:
            return get_floor_ceil(list,mid,target)
        elif target > list[mid]:
            l = mid + 1
            floor = mid
        else:
            r = mid - 1
            ceil = mid
    return floor,ceil   

def get_floor_ceil(list,mid,target):
    i = j = mid
    l = len(list) 
    while i>=0 and i<l:
        if list[i] == target:
            i = i - 1
        else:
            break
    while j>=0 and j<l:
        if list[j] == target:
            j = j + 1
        else:
            break
    return i+1, j-1

if __name__ == "__main__":
    arr = [0,1,2,4,4,4,4,4,4,4,4,4,5,6]
    print(binary_search(arr,3))
    print(binary_search_recursion(arr,3))
    print(binary_search_floor_ceil(arr,3))