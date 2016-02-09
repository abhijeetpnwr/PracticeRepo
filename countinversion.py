import math


class Solution:
	def countInversion(self,A):
		ourarr = A
		self.breakarr(A)

	def merges(self,A):
		size_arr = len(A)
		
		if size_arr<=1:
			print("Time to stop")
			return

		if size_arr%2!=0:
			mid = math.ceil(size_arr/2)
		else:
			mid = int(size_arr/2)
	
		self.merges(A[0:mid])
		self.merges(A[mid:size_arr])


	
sal = Solution()

numlist = [2, 4, 1, 3, 5 ,8 , 10]
sal.merges(numlist)
     

