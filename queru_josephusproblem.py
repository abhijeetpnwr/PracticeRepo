# Querue implementation to solve josephus problem

class queueimpl:
	def __init__(self):
		self.items = []
	def enqueue(self, item):
		self.items.insert(0,item)
	def dequeue(self):
		return self.items.pop()
	def size(self):
		return len(self.items)
	def __str__(self):
		concatstr = ""
		for i in range (0,len(self.items)):
			if i == 0:
				concatstr = concatstr+str(self.items[i])
			else:
				concatstr = concatstr+"  "+str(self.items[i])

		return concatstr

soldierqueue = queueimpl()

for i in range (1,101):
	soldierqueue.enqueue(i)

setcount = 2
startcount = 0

while soldierqueue.size()!=1:
	if startcount == setcount-1:
		startcount = 0
		soldierqueue.dequeue()
	else:
		temp = soldierqueue.dequeue()
		soldierqueue.enqueue(temp)
		startcount=startcount+1

print soldierqueue








