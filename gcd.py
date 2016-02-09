#Program to find gcd for two no .

'''

Euclid's algorithm to find gcd of No:
------------------------------------

What Euclid called "common measure" is termed nowadays a common factor or a common divisor. Euclid VII.2 then offers an algorithm for finding the greatest common divisor (gcd) of two integers. Not surprisingly, the algorithm bears Euclid's name.

The algorithm is based on the following two observations:

If b|a then gcd(a, b) = b.
This is indeed so because no number (b, in particular) may have a divisor greater than the number itself (I am talking here of non-negative integers.)

If a = bt + r, for integers t and r, then gcd(a, b) = gcd(b, r).
Indeed, every common divisor of a and b also divides r. Thus gcd(a, b) divides r. But, of course, gcd(a, b)|b. Therefore, gcd(a, b) is a common divisor of b and r and hence gcd(a, b) ≤ gcd(b, r). The reverse is also true because every divisor of b and r also divides a.

Example

Let a = 2322, b = 654.

 	2322 = 654·3 + 360	  	gcd(2322, 654) = gcd(654, 360)
 	654 = 360·1 + 294	  	gcd(654, 360) = gcd(360, 294)
 	360 = 294·1 + 66	  	gcd(360, 294) = gcd(294, 66)
 	294 = 66·4 + 30	  	gcd(294, 66) = gcd(66, 30)
 	66 = 30·2 + 6	  	gcd(66, 30) = gcd(30, 6)
 	30 = 6·5	  	gcd(30, 6) = 6
Therefore, gcd(2322,654) = 6.

'''

m = 137
n = 30

stopbool = False
stopc = 0

while m%n !=0:
	
	stopc = stopc+1
	if stopc ==50:
		break

	tempn = m%n 
	m = n
	n = tempn

if stopc == 50:
	print " ----- Terminating condition met ----" 
else:
	print "Should print gcd",n



