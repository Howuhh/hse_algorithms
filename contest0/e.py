
def count_del(string):
	count = 0
	
	i = 0
	while ord(string[i]) == 39:
		count += 1
		i += 1
	return count

def edit_string(string):
	if string.startswith("'"):
		string = string[2*count_del(string):]
	if string.endswith("'"):
		string = string[:-2*count_del(string[::-1])]

	return string

string = input().split()
print("".join([edit_string(s) for s in string]))
