#Problem Description
"""
Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.

NOTE: You should make minimum number of comparisons.
"""
#Examle Input and Output
"""
Example Input
Input 1:

 A = [-2, 1, -4, 5, 3]
Input 2:

 A = [1, 3, 4, 1]


Example Output
Output 1:

 1
Output 2:

 5


Example Explanation
Explanation 1:

 Maximum Element is 5 and Minimum element is -4. (5 + (-4)) = 1. 
Explanation 2:

 Maximum Element is 4 and Minimum element is 1. (4 + 1) = 5.
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        min,max=A[0],A[0]
        for i in range(len(A)):
            if(max<A[i]):
                max=A[i]
            if(min>A[i]):
                min=A[i]    
        return min+max
#or
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        return max(A)+min(A)
