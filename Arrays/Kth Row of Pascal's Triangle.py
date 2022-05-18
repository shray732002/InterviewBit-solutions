#Problem Description
"""
Given an index k, return the kth row of the Pascal's triangle.
Pascal's triangle: To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1.

Example:

Input : k = 3


Return : [1,3,3,1]

Note: k is 0 based. k = 0, corresponds to the row [1]. 

Note: Could you optimize your algorithm to use only O(k) extra space?
"""
def fact(n):
    if(n==0):
        return 1
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    return factorial    
class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        res=[0]*(A+1)
        for i in range(0,A+1):
            res[i]=fact(A)//(fact(i)*fact(A-i))
        return res    
