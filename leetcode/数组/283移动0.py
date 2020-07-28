#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 13:51
# @Author  : chenshiyang
# @Site    : 
# @File    : 283移动0.py
# @Software: PyCharm

def move_zero(arr):
    """
    1.新定义一个数组nums，将原数组中arr不为0的数组添加到新数组nums
    2.遍历新数组nums，将原数组前部分设置为不为0的数 arr[i] = nums[i]
    3.将原数组nums后部分设置为0

    时间复杂度为O(n) 空间复杂度为O(n)
    """

    if arr is None:return None

    nums = []
    for i in arr:
        if i:
            nums.append(i)

    for i in range(len(nums)):
        arr[i] = nums[i]

    for i in range(len(nums), len(arr)):
        arr[i] = 0

    return arr

arr = [0,13,23,0,45]
# print(move_zero(arr))

def move_zero1(arr):
    """
    不使用临时数组
    1.定义一个新变量k=0
    2.遍历数组arr，如果元素i不为0 arr[k] = i, k+=1
    3.将数组arr 从k开始剩余位置设置为0

    时间复杂度依旧为O(n)
    """

    k = 0
    for i in arr:
        if i:
            arr[k] = i
            k += 1

    for i in range(k, len(arr)):
        arr[i] = 0

    return arr

# print(move_zero1(arr))

def move_zero2(arr):
    """
    元素原地交换
    """

    k = 0
    for i in range(len(arr)):
        if arr[i]:
            if i != k:
                arr[k] ,arr[i] = arr[i], arr[k]
                k += 1
            else:
                k += 1

    return arr
print(move_zero2(arr))