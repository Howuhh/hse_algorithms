from heapq import heappop, heappush, heapify

# point a - O(nk), like insertion sort
def insertion_sort(arr, k):
	arr = arr[:]

	for i in range(len(arr)):  # O(n)
		j = i

		while j > 0 and arr[j] <= arr[j - 1]:  # O(k)
			arr[j], arr[j - 1] = arr[j - 1], arr[j]
			j = j - 1
	return arr

# point d - O(nlogk)
def inversion_heap_sort(arr, k):
	sorted_arr = []
	heap = arr[:k+1]

	heapify(heap)

	for i in range(k + 1, len(arr)):
		sorted_arr.append(heappop(heap))
		heappush(heap, arr[i])

	while heap:
		sorted_arr.append(heappop(heap))

	return sorted_arr


