
def cutter(people_array):
	people_count = len(people_array)
	cutter_checker = 0
	saved_people = []
	no_people = len(people_array)
	for people_count in people_array:
			if(cutter_checker%2 == 0):
				saved_people.append(people_array[cutter_checker])
			cutter_checker = cutter_checker+1
	return saved_people		

def swap_people(people_array):
	swapped_array = []
	people_count = len(people_array)
	swapped_array.append(people_array[people_count-1])
	for i in range(people_count - 1):
		swapped_array.append(people_array[i])

	return swapped_array

people_array = range(1,778)

loopcount = 0

while loopcount<10:
	people = len(people_array)
	print("Total no. of people in input",people)
	print("Input array is :",people_array)

	print("\n") 
	if(people%2 == 0):
		people_array = cutter(people_array)

	else:
		print("odd no. of people , so at end last member will have knife with him, so he is the first one for the next round")
		people_array = swap_people(cutter(people_array))

	print("Returned array is:",people_array)
	print("----------------------------------------------------")
	loopcount = loopcount +1	 


