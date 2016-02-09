## Motive of script is to genreate randowm between 1 and a given prime no. 
import time
import math

prevtime = time.time()
print prevtime

end_limit = 10000000
print "Need to genrate priime till :",end_limit
start = 2
primearr = []
primearr.append(start)
primearr.append(start+1)

print primearr

for probableprime in range (start+1,end_limit,2):
	primecheck = True
	for foundprime in primearr:
		if foundprime>math.sqrt(probableprime):
			break
		if probableprime%foundprime == 0:
			primecheck=False
			break

	if primecheck:
		primearr.append(probableprime)

print "Found primes are :",primearr

currtime = time.time()
diff = currtime-prevtime

print "Done in:",diff


