#Problem Description

"""
Hamming distance between two non-negative integers is defined as the number of positions at which the corresponding bits are different.

Given an array A of N non-negative integers, find the sum of hamming distances of all pairs of integers in the array. Return the answer modulo 1000000007.
"""

"""
Example Input
Input 1:

 A = [1]
Input 2:

 A = [2, 4, 6]


Example Output
Output 1:

 0
Output 2:

 8


Example Explanation
Explanation 1:

 No pairs are formed.
Explanation 2:

 We return, f(2, 2) + f(2, 4) + f(2, 6) + f(4, 2) + f(4, 4) + f(4, 6) + f(6, 2) + f(6, 4) + f(6, 6) = 8
"""
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def hammingDistance(self, A):
        lst=[]
        for i in range(len(A)):
            lst.append(A[i])
        n=len(lst)
        
        ans=0
        for i in range(0,32):
            count_1=0
            count_0=0
            for j in range(n):
                if lst[j]%2==0:
                    count_0+=1
                else:
                    count_1+=1
                lst[j]=int(lst[j]/2)
            ans+= (count_1*count_0*2)
        return ans%1000000007 
