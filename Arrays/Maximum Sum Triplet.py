#Problem Description
"""
Given an array A containing N integers.

You need to find the maximum sum of triplet ( Ai + Aj + Ak ) such that 0 <= i < j < k < N and Ai < Aj < Ak.

If no such triplet exist return 0.
"""
#Example Input and Output
"""
Example Input
Input 1:

 A = [2, 5, 3, 1, 4, 9]
Input 2:

 A = [1, 2, 3]


Example Output
Output 1:

 16
Output 2:

 6


Example Explanation
Explanation 1:

 All possible triplets are:-
    2 3 4 => sum = 9
    2 5 9 => sum = 16
    2 3 9 => sum = 14
    3 4 9 => sum = 16
    1 4 9 => sum = 14
  Maximum sum = 16
Explanation 2:

 All possible triplets are:-
    1 2 3 => sum = 6
 Maximum sum = 6

"""
from bisect import bisect_left
def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i:
        return i - 1
    else:
        return -1
class Solution:
    # @param A : list of integers
    # @return an integer
 
 def solve(self , A):
    n=len(A)
    rightsuff = [0] * n
    rightsuff[n - 1] = A[n - 1]
    for i in range(n - 2, -1, -1):
        rightsuff[i] = max(rightsuff[i + 1], A[i])
    lst = []
    maxe = 0
    lst.append(A[0])
    for i in range(1, n - 1):
        res = BinarySearch(lst, A[i])
        if res != -1 and A[i] < rightsuff[i + 1]:
            ans = lst[res] + A[i] + rightsuff[i + 1]
            maxe = max(maxe, ans)
        lst.insert(res + 1, A[i])
    return maxe
    return 0
