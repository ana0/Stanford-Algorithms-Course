unsorted = [1,4,6,3,2,9,4,2,5,2,8,67,23,3,5,7,9,42]

def merge_sort(to_sort):
	if len(to_sort) <= 1:
		return to_sort
	a_list = merge_sort(to_sort[0:len(to_sort)/2])
	b_list = merge_sort(to_sort[len(to_sort)/2:len(to_sort)])
	_sorted = []
	a = 0
	b = 0
	for i in range(len(to_sort)):
		try:
			if a_list[a] <= b_list[b]:
				_sorted.append(a_list[a])
				a += 1 
			elif b_list[b] < a_list[a]:
				_sorted.append(b_list[b])
				b += 1 
		except IndexError:
			if a == len(a_list):
				_sorted += b_list[b:]
				break
			_sorted += a_list[a:]
			break

	return _sorted

def merge_sort_2(to_sort):
	if len(to_sort) <= 1:
		return to_sort
	a_list = merge_sort(to_sort[0:len(to_sort)/2])
	b_list = merge_sort(to_sort[len(to_sort)/2:len(to_sort)])
	_sorted = []
	a = 0
	b = 0
	while a < len(a_list) and b < len(b_list):
		if a_list[a] <= b_list[b]:
			_sorted.append(a_list[a])
			a += 1 
		elif b_list[b] < a_list[a]:
			_sorted.append(b_list[b])
			b += 1 
	_sorted += a_list[a:]
	_sorted += b_list[b:]
	return _sorted

print sorted(unsorted)
print merge_sort(unsorted)