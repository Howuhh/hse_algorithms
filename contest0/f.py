import sys
import re

strings = sys.stdin.readlines()

for string in strings:
	new_s = string.replace("viki", "entsiklo").replace("-", "v")
	sys.stdout.write(new_s)
