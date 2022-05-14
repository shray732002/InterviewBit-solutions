#Problem Description

"""A items are to be delivered in a circle of size B.

Find the position where the Ath item will be delivered if we start from a given position C.

NOTE: Items are distributed at adjacent positions starting from C.
"""  
#Example Input
"""Input 1:

 A = 2
 B = 5
 C = 1
Input 2:

 A = 8
 B = 5
 C = 2
"""
#Example Output
"""Output 1:

 2
Output 2:

 4
 """
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        return (C+(A-1))%B
