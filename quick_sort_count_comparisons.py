import random, sys

unsorted = [2,5,7,1,9,3,8,6,4,0]

counter = 0

f = open("test.txt")
_unsorted = [int(line.strip("\n")) for line in f]

def quick_sort_first_pivot(to_sort):
    global counter
    if len (to_sort) <= 1:
        return to_sort
    pivot = to_sort[0]
    to_sort.remove(pivot)
    to_sort.insert(0, pivot)
    i = 1
    for j in range(1,len(to_sort)):
        counter += 1
        if to_sort[j] < pivot:
            to_sort[i], to_sort[j] = to_sort[j], to_sort[i]
            i += 1
    to_sort.remove(pivot)
    to_sort.insert(i-1, pivot)
    print counter
    return quick_sort_first_pivot(to_sort[:i-1]) + quick_sort_first_pivot([to_sort[i-1]]) + quick_sort_first_pivot(
        to_sort[i:])


def quick_sort_last_pivot(to_sort, count):
    # count += len(to_sort)-1
    if len (to_sort) <= 1:
        return to_sort
    pivot = to_sort[-1]
    to_sort.remove(pivot)
    to_sort.insert(0, pivot)
    # count += len(to_sort)-1
    i = 1
    for j in range(1,len(to_sort)):
        if to_sort[j] < pivot:
            to_sort[i], to_sort[j] = to_sort[j], to_sort[i]
            i += 1
    to_sort.remove(pivot)
    to_sort.insert(i-1, pivot)
    count += (len(to_sort[:i])-1)
    count += (len(to_sort[i:])-1) 
    print count
    return quick_sort_last_pivot(to_sort[:i-1], count) + quick_sort_last_pivot(
        to_sort[i-1:], count)

def quick_sort_median_pivot(to_sort, count):
    print to_sort
    if len (to_sort) <= 1:
        return (to_sort, count)
    if len(to_sort) % 2 == 0: 
        mid = len(to_sort)/2 -1
    else: 
        mid = len(to_sort)/2 
    print mid
    if ((to_sort[0] < to_sort[mid]) & (to_sort[0] > to_sort[-1])) | ((
        to_sort[0] > to_sort[mid]) & (to_sort[0] < to_sort[-1])):
        pivot = to_sort[0]
    elif ((to_sort[mid] < to_sort[-1]) & (to_sort[mid] > to_sort[0])) | (
        (to_sort[mid] > to_sort[-1]) & (to_sort[mid] < to_sort[0])):
        pivot = to_sort[mid]
    else:
        pivot = to_sort[-1]
    print pivot
    to_sort.remove(pivot)
    to_sort.insert(0, pivot)
    i = 1
    for j in range(1,len(to_sort)):
        if to_sort[j] < pivot:
            count += 1
            to_sort[i], to_sort[j] = to_sort[j], to_sort[i]
            i += 1
    to_sort.remove(pivot)
    to_sort.insert(i-1, pivot) 
    print to_sort, count
    _sorted_a, count = quick_sort_median_pivot(to_sort[:i-1], count)
    _sorted_b, count = quick_sort_median_pivot(to_sort[i-1:], count)
    return (_sorted_a + _sorted_b, count)


print quick_sort_first_pivot(_unsorted)