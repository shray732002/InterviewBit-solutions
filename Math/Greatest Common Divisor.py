#Problem
"""
Given 2 non negative integers m and n, find gcd(m, n)

GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.

Both m and n fit in a 32 bit signed integer.

Example

m : 6
n : 9

GCD(m, n) : 3 
NOTE : DO NOT USE LIBRARY FUNCTIONS
"""
class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def gcd(self, A, B):
		C=min(A,B)
		D=max(A,B)
		if(C==0):
			return D
		while(1):
			rem=D%C
			if(rem==0):
				return C
            D=C
			C=rem

