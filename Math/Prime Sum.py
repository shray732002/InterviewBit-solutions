#Problem
"""
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

NOTE A solution will always exist. read Goldbach’s  conjecture

Example:


Input : 4
Output: 2 + 2 = 4

If there are more than one solutions possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b,
and [c,d] is another solution with c <= d, then

[a, b] < [c, d] 

If a < c OR a==c AND b < d.
"""
def checkprime(num):
        for n in range(2,int(num**0.5)+1):
         if num%n==0:
            return False
        return True
class Solution:
	# @param A : integer
	# @return a list of integers
  
	def primesum(self, A):
        lst=[]
        for i in range(2,A-1):
            if(checkprime(i) and checkprime(A-i)):
                lst.append(i)
                lst.append(A-i)
                return lst
