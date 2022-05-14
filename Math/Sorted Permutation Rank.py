#Problem
"""
Given a string, find the rank of the string amongst its permutations sorted lexicographically. 

Assume that no characters are repeated.

Example :

Input : 'acb'
Output : 2

The order permutations with letters 'a', 'c', and 'b' : 
abc
acb
bac
bca
cab
cba
The answer might not fit in an integer, so return your answer % 1000003
"""
def fact( n) :
	factorial=1
	for i in range(1,n + 1):
       factorial = factorial*i
	return factorial   
def solve(lst,rank,N):
	for i in range(N):
		lst1=lst[:]
	    lst1.sort()
		n=len(lst)
        idx=lst1.index(lst[0])
        rank+=((idx-0)*fact(n-1))
	    lst.pop(0)
	    
	return (rank+1)%1000003

	
class Solution:
	# @param A : string
	# @return an integer
	def findRank(self, A):
		lst=[]
		rank=0
		for i in range(len(A)):
			lst.append(A[i])
		N=len(A)		
		rank+=solve(lst,rank,N)
		return rank
