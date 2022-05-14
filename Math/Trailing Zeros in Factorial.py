#Problem Description
"""
Given an integer A, return the number of trailing zeroes in A!.

Note: Your solution should be in logarithmic time complexity.
"""
#Example Input and Output
"""
Example Input
Input 1:

 A = 4
Input 2:

 A = 5


Example Output
Output 1:

 0
Output 2:

 1


Example Explanation
Explanation 1:

 4! = 24
Explanation 2:

 5! = 120
"""
class Solution:
	# @param A : integer
	# @return an integer
	def trailingZeroes(self, n):
		if(n < 0):
            return -1
        count = 0
        while(n >= 5):
           n=n//5
           count += n
        return count
