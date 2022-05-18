#Problem Description
"""
Given an integer array A of size N.

You need to check that whether there exist a element which is strictly greater than all the elements on left of it and strictly smaller than all the elements on right of it.

If it exists return 1 else return 0.

NOTE:

Do not consider the corner elements i.e A[0] and A[N-1] as the answer.
"""
#Example Input and Output
"""
Example Input
Input 1:

 A = [5, 1, 4, 3, 6, 8, 10, 7, 9]
Input 2:

 A = [5, 1, 4, 4]


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 A[4] = 6 is the element we are looking for.
 All elements on left of A[4] are smaller than it and all elements on right are greater.
Explanation 2:

 No such element exits.
 """
class Solution:
    # @param A : list of integers
    # @return an integer
  def perfectPeak(self, A):
    n = len(A)
    count=0
    minr = [0] * n
    maxl = [0] * n
    maxl[0] = A[0]
    maxL = A[0]
    minr[n-1]=A[n-1]
    minR=A[n-1]
    for i in range(1, n):
        maxl[i] = maxL
        if (maxL < A[i]):
            maxL = A[i]
    for i in range(n-1,-1,-1):
        minr[i]=minR
        if(minR>A[i]):
            minR=A[i]
    for i in range(1,len(A)-1):
        if(A[i]>maxl[i] and A[i]<minr[i]):
            count+=1
    if(count>0):
        return 1
    else:
        return 0            
