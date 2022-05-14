#Problem Description

"""Given the position of a Bishop (A, B) on an 8 * 8 chessboard.
Your task is to count the total number of squares that can be visited by the Bishop in one move.
The position of the Bishop is denoted using row and column number of the chessboard."""

#Example Input
"""Input 1:

 A = 4
 B = 4"""
#Example Output
"""Output 1:

 13"""



class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, x, y):
     if x>y:
        count=(8-x+y-1)
     else:
        count=(8-y+x-1)
    
     if(x+y<=8):
        res=y-1
        xnew=x+res
        ynew=1
        count+=abs(xnew-ynew)
     else:
        res=8-x
        xnew=8
        ynew=y-res
        count+=abs(xnew-ynew)
     return count   
