#Program to infix to postfix and prefix conversion

class stackimpl:
	
	def __init__(self):
		elemlist = []
		self.elemlist = elemlist

	def push(self,element):
		self.elemlist.append(element)


	def pop(self):
		if len(self.elemlist)==0:
			return 
		elem = self.elemlist.pop()
		return elem

	def show(self):
		return self.elemlist

	def __len__(self):
		return len(self.elemlist)

	def showlastelem(self):
		lastindex  = len(self.show())-1
		lastelem = self.elemlist[lastindex]
		return lastelem
		


#Empty stack opstack for keeping operators
opstack = stackimpl()

#List to save output of it
outputlist = []

#Operand list 
operandlist = ["*","/","+","-","(",")"]

expression = 'A+B*C-D'

def pref(mychar):
	if mychar == "/" or mychar =="*":
		return 2
	if mychar == "+" or mychar == "-":
		return 1

for c in expression:
	if c in operandlist:
		if c == ")":
			stopcond = False
			
			while stopcond == False:
				
				poppedelem = opstack.pop()
				
				if poppedelem == "(":
					stopcond = True
				else:
					outputlist.append(poppedelem)

		else:
			if len(opstack)>0 and opstack.showlastelem()!="(" and c!= "(" and (pref(c)<pref(opstack.showlastelem())):
				outputlist.append(opstack.pop())
			opstack.push(c)	
			#print "Output list :",outputlist
			#print opstack.show()
	else:
	 outputlist.append(c)

while len(opstack)!=0:
	outputlist.append(opstack.pop())

print "Postfix result for the expression is :"," ".join(outputlist)



