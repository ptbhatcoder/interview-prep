'''
Question : In an array having positive integers, except for one number which occurs odd number of times, all other numbers occur even number of times. Find the number.
Link : http://www.ideserve.co.in/learn/find-the-number-which-occurs-odd-number-of-times
Algorithm : Initialise a temporary variable and xor it with all the elements in the array one by one, the other elements will cancel each other and our candidate remains
Complexity : O(n)
Test-inputs : 
1. empty list : [] --> "empty"
2. single element : [3] --> the element
3. list with all elements occuring even number of times --> "invalid"
4. list with multiple elements occuring odd number of times --> "invalid"
5. list with '0' occuring odd number of times --> 0
6. list with some element x occuring odd number of time --> element x
'''
import unittest
import random
# the unit or the method
def findOddOccuringElement(inputArray):
	if not len(inputArray):
		return "empty"
	runner = 0
	for elem in inputArray:
		runner^=elem
	
	#now run once more to check if it is genuine or invalid test cases 3,4
	count = inputArray.count(runner)
	if count and count&1:
		# means we have found the right candidate
		return runner
	return "invalid"
		

# the unit tests with test cases
class findOddOccuringElementTests(unittest.TestCase):
	# the unit tests
	
	#	1. empty list : [] --> "empty"
	def testCase1(self):
		self.failUnless(findOddOccuringElement([])=="empty")
		
	#   2. single element : [3] --> the element
	def testCase2(self):
		temp = random.randint(0,1000)
		self.failUnless(findOddOccuringElement([temp])==temp)
	

	#   3. list with all elements occuring even number of times --> "invalid"
	def testCase3(self):
		self.failUnless(findOddOccuringElement([2,3,4,4,3,3,3,2])=="invalid")
	
	#   4. list with multiple elements occuring odd number of times --> "invalid"
	def testCase4(self):
		self.failUnless(findOddOccuringElement([2,3,4,4,5,5,5,5,6,6,6,6,6])=="invalid")
		
	#   5. list with '0' occuring odd number of times --> 0
	def testCase5(self):
		self.failIf(findOddOccuringElement([0,4,4,4,4,5,5,5,5,6,6,6,6,6,6]))
		
	#   6. list with some element x occuring odd number of time --> element x
	def testCase6(self):
		temp = random.randint(0,1000)
		self.failUnless(findOddOccuringElement([temp,4,4,4,4,5,temp,5,5,5,6,6,6,6,6,6,temp])==temp)
	
if __name__ == '__main__':
	unittest.main()
