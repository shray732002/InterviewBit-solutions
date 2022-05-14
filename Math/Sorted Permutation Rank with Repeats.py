#Problem
"""
Given a string, find the rank of the string amongst its permutations sorted lexicographically. 

Note that the characters might be repeated. If the characters are repeated, we need to look at the rank in unique permutations. 

Look at the example for more details.

Example :

Input : 'aba'
Output : 2

The order permutations with letters 'a', 'a', and 'b' : 
aab
aba
baa
The answer might not fit in an integer, so return your answer % 1000003

NOTE: 1000003 is a prime number

NOTE: Assume the number of characters in string < 1000003
"""
def fact( n) :
	factorial=1
	for i in range(2,n + 1):
       factorial = factorial*i
	return factorial
def solve(lst,N):
    rank=0
    for i in range(N):
        mydict={}
        for i in lst:
            if i not in mydict:
                mydict[i]=1
            else:
                mydict[i]+=1
        lst1=list(mydict.keys())
        lst1.sort()
        idx=0
        j=lst1.index(lst[0])
        for i in range(j):
            idx+=mydict[lst1[i]]
        fact_den=1
        for i in mydict:
            fact_den*=fact(mydict[i])
        fact_num=fact(len(lst)-1)
        fact_num=fact_num*idx
        rank+=(fact_num//fact_den)
        lst.pop(0)
    return rank        
        
class Solution:
	# @param A : string
	# @return an integer
	def findRank(self, A):
        lst=[]
        for i in range(len(A)):
            lst.append(A[i])
        N=len(lst)   
        rank=solve(lst,N)    
        return (rank+1)%1000003
