from math import inf
from bisect import bisect_left, bisect_right

# point a - log^2(n)
def merged_median_naive(arr1, arr2):
	part_size = (len(arr1) + len(arr2)) // 2

	left, right = 0, len(arr1)
	while left <= right:
		mid = (left + right) // 2
		split = bisect_right(arr2, arr1[mid - 1])
		
		if mid + split == part_size:
			break
		elif mid + split < part_size:
			left = mid + 1
		else:
			right = mid - 1

	left_x, left_y = arr1[mid - 1], arr2[part_size - mid - 1]
	right_x, right_y = arr1[mid], arr2[part_size - mid]

	if (len(arr1) + len(arr2)) % 2 == 0:
		return (max(left_x, left_y) + min(right_x, right_y)) // 2
	return min(left_x, left_y)


# point b - log(n)
def merged_median(arr1, arr2):
	part_size = (len(arr1) + len(arr2)) // 2
	
	left, right = 0, len(arr1)
	while left <= right:
		mid = (left + right) // 2
		
		left_x, left_y = arr1[mid - 1], arr2[part_size - mid - 1]
		right_x, right_y = arr1[mid], arr2[part_size - mid]
		
		if left_x <= right_y and left_y <= right_x:
			# return mid, part_size - mid
			break
		elif left_x > right_y:
			right = mid - 1
		else:
			left = mid + 1

	if (len(arr1) + len(arr2)) % 2 == 0:
		return (max(left_x, left_y) + min(right_x, right_y)) // 2
	return min(left_x, left_y)



def k_smallest_naive(arr1, arr2, k):
	left = min(arr1[0], arr2[0])
	right = max(arr1[-1], arr2[-1])

	while left <= right:
		mid = (left + right) // 2

		smaller = bisect_right(arr1, mid) + bisect_right(arr2, mid)

		if smaller == k:
			return mid
		elif smaller < k:
			left = mid + 1
		else:
			right = mid - 1

	return left


def k_smallest(a, b, k):

	left, right = 0, len(a) - 1
	while left <= right:
		i = (left + right) // 2
		j = k - 1 - i


		a_left = a[i - 1] if i - 1 >= 0 else -inf
		b_left = b[j - 1] if j - 1 >= 0 else -inf

		if a_left < b[j] < a[i]:
			return a[i]
		elif b_left < a[i] < b[j]:
			return b[j]
		elif a[i] < b[j]:
			left = i + 1
		else:
			right = i - 1

	return -1



# def k_smallest(arr1, arr2, k):
# 	if len(arr1) + len(arr2) < k:
# 		return -1
# 	if k == 1:
# 		return min(arr1[0], arr2[0])
# 	if len(arr1) + len(arr2) == k:
# 		return max(arr1[-1], arr2[-1])

# 	left, right = 0, min(k - 1, len(arr1))
# 	while left <= right:
# 		print(left, right)

# 		i = (left + right) // 2
# 		j = k - 1 - i

# 		if arr2[j - 1] > arr1[i]:
# 			left = i + 1
# 		elif arr1[i - 1] > arr2[j]:
# 			right = i - 1
# 		else:
# 			return min(arr1[i], arr2[j])
	
# 	return -1




def kthSmallestFast(arr1, arr2, k):
	size1, size2 = len(arr1), len(arr2)

	index1, index2, step = 0, 0, 0
	while index1 + index2 < k - 1:
		step = (k - index1 - index2) // 2
		step1 = index1 + step 
		step2 = index2 + step
		if size1 > step1 - 1 and (size2 <= step2 - 1 or arr1[step1 - 1] < arr2[step2 - 1]):
			index1 = step1
		else:
			index2 = step2

	if size1 > index1 and (size2 <= index2 or arr1[index1] < arr2[index2]):
		return arr1[index1]
	else:
		return arr2[index2]