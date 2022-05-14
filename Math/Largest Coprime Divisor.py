#Problem Description
"""
You are given two positive numbers A and B. You need to find the maximum valued integer X such that:

X divides A i.e. A % X = 0
X and B are co-prime i.e. gcd(X, B) = 1
For example,

A = 30
B = 12
We return
X = 5
"""
def gcd(A,B):
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
class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
    
	def cpFact(self, A, B):
        while(gcd(A,B)!=1):
			A=int(A/gcd(A,B))
		return A	
