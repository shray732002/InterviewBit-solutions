#Problem description
"""
Given a target A on an infinite number line, i.e. -infinity to +infinity.

You are currently at position 0 and you need to reach the target by moving according to the below rule:

In ith move you can take i steps forward or backward.
Find the minimum number of moves required to reach the target.
"""
#Input and output Example
"""
Example Input
Input 1:

 3
Input 2:

 2


Example Output
Output 1:

 2
Output 2:

 3


Example Explanation
Explanation 1:

 On the first move we step from 0 to 1.
 On the second step we step from 1 to 3.
Explanation 2:

 On the first move we step from 0 to 1.
 On the second move we step  from 1 to -1.
 On the third move we step from -1 to 2.
"""
from math import sqrt
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        A = abs(A)
        
        last = int(sqrt(1 + 8*A) - 1) // 2
        running_sum = (last * (last + 1)) // 2

        while (running_sum < A) or (running_sum - A) % 2 != 0:
            last += 1
            running_sum += last

        return last 
