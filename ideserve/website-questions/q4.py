'''
Q4 : Given two integer arrays where second array is duplicate of first array with just 1 element missing. Find the element
Author : ptbhatcoder
Method : Exor through all the elements of both the arrays, since xor of two same elements cancel each other, all the elements in the duplicate array cancel out the ones in the original array, leaving behind the missing element in the duplicate array.
Complexity : Time : O(2n) = O(n) where n is the size of either of the arrays, space complexity if O(1) for additional variable
Test cases : 

1) Two normal arrays with missing element(can be zero)
2) A single element array and an empty duplicate
3) No missing element in the duplicate array
4) Multiple missing elements in the duplicate array ( one of them can be zero)
P.S : if an element occurs 'x' times in the original array and 'x-1' times in the duplicate array, then the element is said to be missing as per the definition of the question, since 'x-1' elements match each other
'''

import unittest
import random

def getMissing(orig,dup):
    if len(orig) <= len(dup):
        return None
    if len(orig) > len(dup) + 1:
        return "invalid"
    runner = 0
    for elem in orig:
        runner^=elem
    for elem in dup:
        runner^=elem
    return runner

class TestMissingInDuplicate(unittest.TestCase):
    #Two normal arrays with non missing zero
    #A single element array and an empty duplicate
    def testCase1and2(self):
        n=random.randint(0,1000)
        orig=[]
        while n:
            n-=1
            orig.append(random.randint(0,100000))
        dup=[]
        for elem in orig:
            dup.append(elem)
        pos = random.randint(0,len(orig))
        miss = random.randint(0,100000)
        orig.insert(pos,miss)
        
        self.failUnless(getMissing(orig,dup)==miss)
    
    #No missing element in the duplicate array
    def testCase3(self):
        n=random.randint(0,1000)
        orig=[]
        while n:
            n-=1
            orig.append(random.randint(0,100000))
        dup=[]
        for elem in orig:
            dup.append(elem)
        self.failUnless(getMissing(orig,dup)==None)
    
    #Multiple missing elements in the duplicate array ( one of them can be zero)
    def testCase4(self):
        n=random.randint(0,1000)
        orig=[]
        while n:
            n-=1
            orig.append(random.randint(0,100000))
        dup=[]
        for elem in orig:
            dup.append(elem)
        pos = random.randint(0,len(orig))
        miss = random.randint(0,100000)
        orig.insert(pos,miss)
        
        pos = random.randint(0,len(orig))
        miss = random.randint(0,100000)
        orig.insert(pos,miss)
        
        self.failUnless(getMissing(orig,dup)=="invalid")

if __name__ == '__main__':
    unittest.main()

        
        
        
