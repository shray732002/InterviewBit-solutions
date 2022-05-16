#Problem
"""
Find the contiguous subarray within an array, A of length N which has the largest sum.
"""
#Example Input and Output
"""
Input 1:
    A = [1, 2, 3, 4, -10]

Output 1:
    10

Explanation 1:
    The subarray [1, 2, 3, 4] has the maximum possible sum of 10.

Input 2:
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output 2:
    6

Explanation 2:
    The subarray [4,-1,2,1] has the maximum possible sum of 6.
"""
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        maxv=-2147483648
        sumv=0
        n=len(A)
        for i in range(n):
            sumv+=A[i]
            if(sumv>maxv):
                maxv=sumv
            if(sumv<0):
                sumv=0    
        return maxv 
