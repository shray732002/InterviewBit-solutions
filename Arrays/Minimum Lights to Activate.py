#Problem Description
"""
There is a corridor in a Jail which is N units long. Given an array A of size N. The ith index of this array is 0 if the light at ith position is faulty otherwise it is 1.

All the lights are of specific power B which if is placed at position X, it can light the corridor from [ X-B+1, X+B-1].

Initially all lights are off.

Return the minimum number of lights to be turned ON to light the whole corridor or -1 if the whole corridor cannot be lighted.
"""
#Example Input and Output
"""
Example Input
Input 1:

A = [ 0, 0, 1, 1, 1, 0, 0, 1].
B = 3
Input 2:

A = [ 0, 0, 0, 1, 0].
B = 3


Example Output
Output 1:

2
Output 2:

-1


Example Explanation
Explanation 1:

In the first configuration, Turn on the lights at 3rd and 8th index.
Light at 3rd index covers from [ 1, 5] and light at 8th index covers [ 6, 8].
Explanation 2:

In the second configuration, there is no light which can light the first corridor.
"""
def findIndex(A,to,pos):
    for i in range(to,pos-1,-1):
        if(A[i]==1):
            return i
    return -1        
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        pos=0
        count=0
        while(pos<len(A)):
            to=pos+B-1
            if(to>=len(A)):
                to=len(A)-1
            idx=findIndex(A,to,to-(2*B-2))
            if(idx==-1):
                return -1
            pos=idx+B
            count+=1
        return count
