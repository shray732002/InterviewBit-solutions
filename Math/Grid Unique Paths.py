#Problem
"""
A robot is located at the top-left corner of an A x B grid 
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).

How many possible unique paths are there?

Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.
"""
#Example
"""
Input : A = 2, B = 2
Output : 2

2 possible routes : (0, 0) -> (0, 1) -> (1, 1) 
              OR  : (0, 0) -> (1, 0) -> (1, 1)
"""
def fact(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial = factorial * i
    return factorial
class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def uniquePaths(self, A, B):
        fact_num=fact(A+B-2)
        fact_den=fact(A-1)*fact(B-1)
        return fact_num//fact_den
