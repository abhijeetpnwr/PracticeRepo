######## Program to check valid expression ########

class stackimpl:
	def __init__(self):
		elemlist = []
		self.elemlist = elemlist
		print "Stack impl class instatiated"

	def push(self,element):
		self.elemlist.append(element)


	def pop(self):
		if len(self.elemlist)==0:
			return
		elem = self.elemlist.pop()
		return elem

expr = "((3+(2%1)))"
operatorstack = stackimpl()
balancecheck = True

for c in expr:
	if c == '(':
		operatorstack.push(c)
	if c == ')':
		if operatorstack.pop() == None:
			balancecheck = False
			break

if balancecheck == True and len(operatorstack.elemlist)==0:
	print "Your expression was valid"

else:
	print "Not a valid expression"

