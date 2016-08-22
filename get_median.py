def get_mid(to_sort):
    if len(to_sort) % 2 == 0: 
        mid = len(to_sort)/2 -1
    else: 
        mid = len(to_sort)/2 
    print mid
    if ((to_sort[0] < to_sort[mid]) & (to_sort[0] > to_sort[-1])) | ((to_sort[0] > 
        to_sort[mid]) & (to_sort[0] < to_sort[-1])):
        pivot = to_sort[0]
    elif ((to_sort[mid] < to_sort[-1]) & (to_sort[mid] > to_sort[0])) | (
        (to_sort[mid] > to_sort[-1]) & (to_sort[mid] < to_sort[0])):
        pivot = to_sort[mid]
    else:
        pivot = to_sort[-1]
    print pivot


get_mid([1,2,8,9,6])
get_mid([5,4,1,2,3])
