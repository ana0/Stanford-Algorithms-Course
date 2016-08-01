import random

unsorted = [2,5,7,1,9,3,8,6,4,0]

def quick_sort(to_sort):
	if len (to_sort) <= 1:
		return to_sort
	pivot = random.choice(to_sort)
	to_sort.remove(pivot)
	to_sort.insert(0, pivot)
	i = 1
	for j in range(1,len(to_sort)):
		if to_sort[j] < pivot:
			to_sort[i], to_sort[j] = to_sort[j], to_sort[i]
			i += 1
	to_sort.remove(pivot)
	to_sort.insert(i-1, pivot)
	return quick_sort(to_sort[:i]) + quick_sort(to_sort[i:])


print quick_sort(unsorted)