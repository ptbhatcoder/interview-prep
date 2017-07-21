'''
Question : Implement comb sort
Complexity : O(n^2)( time), O(1) space ( apart from the input array)
Swaps : O(n^2)
Comparisons : O(n^2)
About : It is a modification of the normal bubble sort where instead of consecutive elements of the array, two elements at a dynamically changing distance determined by a scaling factor are compared 
Test cases:
1) Empty input --> None
2) Single element --> input same as output
3) Normal array --> Array sorted
'''

import unittest
import random

# first the unit tests
class CombSortTests(unittest.TestCase):

	#Empty input --> "empty"
	def testCase1(self):
		self.failUnless(combSort([])==None)

	#Single element --> input same as output
	def testCase2(self):
		key = random.randint(0,100000)
		self.failUnless([key]==combSort([key]))

	#Normal array --> Array sorted
	def testCase3(self):
		size = random.randint(1,10)
		inp = []
		while size:
			size-=1
			inp.append(random.randint(0,100000))
		self.failUnless(combSort(inp)==sorted(inp))

def combSort(inp):
	if not len(inp):
		return None
	if len(inp) == 1:
		return inp
	factor = 1.3
	gap = len(inp)
	swapped = True # if in any iteration we did not swap any elements, then we have a sorted array
	
	while gap > 1 or swapped:
		gap = int(gap  / factor)
		swapped = False
		for i in range(len(inp)-gap):
			
			if inp[i] > inp[i+gap]:
				
				swapped = True
				temp = inp[i]
				inp[i] = inp[i+gap]
				inp[i+gap] = temp

	
	return inp

if __name__=='__main__':
	unittest.main()
