#Problem Description
"""
You are given a binary string A(i.e. with characters 0 and 1) consisting of characters A1, A2, ..., AN. In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the characters AL, AL+1, ..., AR. By flipping, we mean change character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised.

If you don't want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.
"""
#Example Input and Output
"""
Example Input
Input 1:

A = "010"
Input 2:

A = "111"


Example Output
Output 1:

[1, 1]
Output 2:

[]


Example Explanation
Explanation 1:

A = "010"


Pair of [L, R] | Final string
____________|__________
[1 1]          | "110"
[1 2]          | "100"
[1 3]          | "101"
[2 2]          | "000"
[2 3]          | "001"



We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].

Explanation 2:

No operation can give us more than three 1s in final string. So, we return empty array [].
"""
class Solution:
    # @param A : string
    # @return a list of integers
  def flip(self, A):
    if (A.count('1') == len(A)):
        return []
    lst = []
    for i in range(len(A)):
        if (A[i] == '0'):
            lst.append(1)
        else:
            lst.append(-1)

    max_so_far = 0
    max_ending = 0
    L = 0
    R = 0
    lst2= [0,0]
    for i in range(len(lst)):
        max_ending = max_ending + lst[i]
        if (max_so_far < max_ending):
            max_so_far = max_ending
            R = i
            lst2[0]=L+1
            lst2[1]=R+1
        if (max_ending < 0):
            max_ending = 0
            L = i + 1
    return lst2
