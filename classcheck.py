#Basic program to start learning object oriented python
#program to work on fractions.

class Fraction:
	#constructor for the object
    def __init__(self,top,bottom):

        self.num = top
        self.den = bottom

    #Method to convert onject to string
    def __str__(self):
    	return str(self.num)+"/"+str(self.den)

    def __add__(self,otherfrac):
    	nom = self.num*otherfrac.den+self.den*otherfrac.num
    	den = self.den*otherfrac.den
    	return str(nom)+" / "+str(den)

myfraction1 = Fraction(3,5)
myfraction2 = Fraction(4,8)

print "First fractional elem. is :",myfraction1

print "Second fractional elem is :",myfraction2

print myfraction1+myfraction2


