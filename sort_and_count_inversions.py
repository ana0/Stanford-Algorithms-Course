unsorted = [1,4,6,2,3,5]
num_inversions = 0

f = open("IntegerArray.txt")
_unsorted = [int(line.strip("\n")) for line in f]

def count_inversions(to_sort, count):
	if len(to_sort) <= 1:
		return (to_sort, count)
	a_list, count_a = count_inversions(to_sort[0:len(to_sort)/2], count)
	b_list, count_b = count_inversions(to_sort[len(to_sort)/2:len(to_sort)], 
		count)
	_sorted = []
	count_all =	count_a + count_b
	a = 0
	b = 0
	while a < len(a_list) and b < len(b_list):
		if a_list[a] <= b_list[b]:
			_sorted.append(a_list[a])
			a += 1 
		elif b_list[b] < a_list[a]:
			_sorted.append(b_list[b])
			b += 1 
			count_all += len(a_list) - a
	else:
		if a == len(a_list):
			_sorted += b_list[b:]
		_sorted += a_list[a:]
		pass
	return (_sorted, count_all)

answer = count_inversions(_unsorted, num_inversions)
print answer[1]


