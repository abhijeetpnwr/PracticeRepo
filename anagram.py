#

test = raw_input()

a_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

stlen = len(test)

finalset = set()

firsttimecheck  = True

for i in range(0,stlen+1,1):
	
	if firsttimecheck ==True:
		for alphabet in a_list:
			finalset.add(alphabet+test)

	for alphabet in a_list:
		temp = test[0:i+1]+alphabet+test[i+1:]
		finalset.add(temp)
			
print len(finalset)
