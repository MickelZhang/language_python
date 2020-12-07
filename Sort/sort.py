#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/12/7 20:33
# @Author  : MickelZhang
# @File    : sort.py
# @Version: Python3.6

# 参考： https://sort.hust.cc/

# 十排序算法
# 冒泡排序：

def bubble_sort(array):
    """
    1.比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
    3.针对所有的元素重复以上的步骤，除了最后一个。
    4.持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
    :param array:
    :return:
    """
    for i in range(1, len(array)):
        for j in range(0, len(array) - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def selection_sort(array):
    """
    1.首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
    2.再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    3.重复第二步，直到所有元素均排序完毕。
    :param array:
    :return:
    """
    for i in range(len(array) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            array[i], array[minIndex] = array[minIndex], array[i]
    return array

def insertion_sort(array):
    """
    1.将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
    .从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
    （如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
    :param array:
    :return:
    """
    for i in range(len(array)):
        preIndex = i-1
        current = array[i]
        while preIndex >= 0 and array[preIndex] > current:
            array[preIndex+1] = array[preIndex]
            preIndex-=1
        array[preIndex+1] = current
    return array

def shell_sort(array):
    """
    选择一个增量序列 t1，t2，……，tk，其中 ti > tj, tk = 1；
    按增量序列个数 k，对序列进行 k 趟排序；
    每趟排序，根据对应的增量 ti，将待排序列分割成若干长度为 m 的子序列，分别对各子表进行直接插入排序。
    仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。
    :param array:
    :return:
    """
    import math
    gap=1
    while(gap < len(array)/3):
        gap = gap*3+1
    while gap > 0:
        for i in range(gap,len(array)):
            temp = array[i]
            j = i-gap
            while j >=0 and array[j] > temp:
                array[j+gap]=array[j]
                j-=gap
            array[j+gap] = temp
        gap = math.floor(gap/3)
    return array

