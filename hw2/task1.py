
def if_possible(min_dist, arr, k):
	count = 1

	last = arr[0]
	for i in range(1, len(arr)):
		if arr[i] - last >= min_dist:
			count += 1
			last = arr[i]
			
			if count == k:
				return True
	print(count)	
	return False 


def max_min_dist(arr, k):
	sorted_arr = sorted(arr)
	left, right = sorted_arr[0], sorted_arr[-1]

	best_dist = 0
	while left <= right:
		min_dist = (left + right) // 2
		
		if if_possible(min_dist, sorted_arr, k):
			best_dist = max(best_dist, min_dist)	
			left = min_dist + 1
		else:
			right = min_dist - 1

	return best_dist


if __name__ == "__main__":
	test = list(range(1, 11))
	assert max_min_dist(test, 5) == 2
