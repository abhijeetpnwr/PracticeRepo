class parent:
	def __init__(self,lastname,eyecolor):
		print "-- Parent constructor called -- \n"
		self.lastname=lastname
		self.eyecolor=eyecolor



class child(parent):
	def __init__(self,lastname,eyecolor,no_of_toys):
		print " -- Child constructor called -- "
		parent.__init__(self,lastname,eyecolor)
		self.no_of_toys=no_of_toys

miley_cyrus = child("Cyrus","Blue",5)

print miley_cyrus.lastname
print miley_cyrus.no_of_toys