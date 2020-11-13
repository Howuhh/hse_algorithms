
def array_add(arr, req):
	pref_add = [0] * (len(arr) + 1)
	pref_sub = [0] * (len(arr) + 1)
	
	for (x, l, r) in req:
		pref_add[l] += x
		pref_sub[r + 1] += -x
	
	total_add = pref_add
	for i in range(1, len(n)):
		total_add[i] = pref_add[i] + pref_add[i - 1] + pref_sub[i]
	
	for i in range(len(arr)):
		arr[i] += total_add[i]
	
	return arr

