import random

unsorted = [2,5,7,1,11,9,3,8,6,4,0,10,12,14,13,17,15,16]

def quick_sort(to_sort):
	if len (to_sort) <= 1:
		return to_sort
	pivot = random.randint(0, len(to_sort)-1)
	to_sort[0], to_sort[pivot] = to_sort[pivot], to_sort[0]
	pivot = to_sort[0]
	i = 1
	for j in range(1,len(to_sort)):
		if to_sort[j] < pivot:
			to_sort[i], to_sort[j] = to_sort[j], to_sort[i]
			i += 1
	to_sort[0], to_sort[i-1] = to_sort[i-1], to_sort[0]
	return quick_sort(to_sort[:i]) + quick_sort(to_sort[i:])

def quick_select(to_sort, goal):
	if len (to_sort) <= 1:
		print to_sort[goal]
		return (to_sort, goal)
	pivot = random.randint(0, len(to_sort)-1)
	to_sort[0], to_sort[pivot] = to_sort[pivot], to_sort[0]
	pivot = to_sort[0]
	i = 1
	for j in range(1, len(to_sort)):
		if to_sort[j] < pivot:
			to_sort[i], to_sort[j] = to_sort[j], to_sort[i]
			i += 1
	to_sort[0], to_sort[i-1] = to_sort[i-1], to_sort[0]
	if i-1 == goal:
		print to_sort[goal]
		return (to_sort, goal)
	elif i-1 > goal:
		quick_select(to_sort[:i-1], goal)
	else:
		goal = goal - i
		quick_select(to_sort[i:], goal)

print quick_select(unsorted, 14)