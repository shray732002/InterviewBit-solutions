#Problem Description
"""
There are A cities numbered from 1 to A. You have already visited M cities, the indices of which are given in an array B of M integers.

If a city with index i is visited, you can visit either the city with index i-1 (i >= 2) or the city with index i+1 (i < A) if they are not already visited.
Eg: if N = 5 and array M consists of [3, 4], then in the first level of moves, you can either visit 2 or 5.

You keep visiting cities in this fashion until all the cities are not visited.
Find the number of ways in which you can visit all the cities modulo 10^9+7.
"""
#Example
"""
For Example 

Input:

A = 5
B = [2, 5]

Output:

6

Explanation:

All possible ways to visit remaining cities are :
1. 1 -> 3 -> 4
2. 1 -> 4 -> 3
3. 3 -> 1 -> 4
4. 3 -> 4 -> 1
5. 4 -> 1 -> 3
6. 4 -> 3 -> 1
"""
def fact(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial = factorial * i
    return factorial
def solve1( A, B, N):
    lst=[]
    B.sort()
    lst.append(B[0]-1)
    for i in range(len(B)-1):
       lst.append(B[i+1]-B[i]-1)
    lst.append(A-B[len(B)-1])
    fact_num=1
    fact_num*=fact(A-N)
    for i in range(1,len(lst)-1):
        if(lst[i]>=1):
         fact_num*=pow(2,lst[i]-1)
    fact_den=1
    for i in lst:
        fact_den*=fact(i)
    return (fact_num//fact_den)%1000000007
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self,A,B):
        N=len(B)
        result = solve1(A,B,N)
        return result
