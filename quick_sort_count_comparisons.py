import random, sys

unsorted = [2,5,7,1,9,3,8,6,4,0]

counter = 0

f = open("IntegerArray1.txt")
_unsorted = [int(line.strip("\n")) for line in f]

def quick_sort_first_pivot(to_sort):
    global counter
    if len (to_sort) <= 1:
        return to_sort
    counter += len(to_sort)-1
    print counter
    pivot = to_sort[0]
    i = 1
    for j in range(1,len(to_sort)):
        if to_sort[j] < pivot:
            to_sort[i], to_sort[j] = to_sort[j], to_sort[i]
            i += 1
    to_sort[0], to_sort[i-1] = to_sort[i-1], to_sort[0]
    return quick_sort_first_pivot(
        to_sort[:i-1]) + [to_sort[i-1]] + quick_sort_first_pivot(to_sort[i:])


def quick_sort_last_pivot(to_sort):
    global counter
    if len (to_sort) <= 1:
        return to_sort
    pivot = to_sort[-1]
    counter += len(to_sort)-1
    to_sort[0], to_sort[-1] = to_sort[-1], to_sort[0]
    i = 1
    for j in range(1,len(to_sort)):
        if to_sort[j] < pivot:
            to_sort[i], to_sort[j] = to_sort[j], to_sort[i]
            i += 1
    to_sort[0], to_sort[i-1] = to_sort[i-1], to_sort[0]
    print counter
    return quick_sort_last_pivot(to_sort[:i-1]) + [to_sort[i-1]] + quick_sort_last_pivot(
        to_sort[i:])

def quick_sort_median_pivot(to_sort):
    global counter
    if len (to_sort) <= 1:
        return to_sort
    if len(to_sort) % 2 == 0: 
        mid = len(to_sort)/2 -1
    else: 
        mid = len(to_sort)/2 
    if ((to_sort[0] < to_sort[mid]) & (to_sort[0] > to_sort[-1])) | ((
        to_sort[0] > to_sort[mid]) & (to_sort[0] < to_sort[-1])):
        pivotindex = 0
    elif ((to_sort[mid] < to_sort[-1]) & (to_sort[mid] > to_sort[0])) | (
        (to_sort[mid] > to_sort[-1]) & (to_sort[mid] < to_sort[0])):
        pivotindex = mid
    else:
        pivotindex = -1
    counter += len(to_sort)-1
    to_sort[0], to_sort[pivotindex] = to_sort[pivotindex], to_sort[0]
    pivot = to_sort[0]
    i = 1
    for j in range(1,len(to_sort)):
        if to_sort[j] < pivot:
            to_sort[i], to_sort[j] = to_sort[j], to_sort[i]
            i += 1
    to_sort[0], to_sort[i-1] = to_sort[i-1], to_sort[0]
    print counter
    return quick_sort_median_pivot(to_sort[:i-1]) + [to_sort[i-1]] + quick_sort_median_pivot(
        to_sort[i:])

def quick_sort_aissams(to_sort, lo, hi):
    global counter
    if hi - lo < 1:
        return
    counter += hi - lo
    pivot = to_sort[lo]
    i = lo+1
    
    for j in range(lo+1, hi+1):
        if to_sort[j] < pivot:
            to_sort[i], to_sort[j] = to_sort[j], to_sort[i]
            i += 1
    to_sort[lo], to_sort[i-1] = to_sort[i-1], to_sort[lo]
    print counter
    quick_sort_aissams(to_sort, lo, i-2)  
    quick_sort_aissams(to_sort, i, hi)

quick_sort_median_pivot(_unsorted)