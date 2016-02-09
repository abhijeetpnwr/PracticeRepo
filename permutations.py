import math
str = "abcd"

def permutations(str1):
	if len(str1) == 0:
		print("End")
	else:			
		permutations(str1[1:])
		print(str1)

dev = math.floor(8/3)

print(dev)