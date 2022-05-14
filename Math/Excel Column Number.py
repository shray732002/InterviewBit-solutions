#Problem Description
"""
Given a column title A as appears in an Excel sheet, return its corresponding column number.
"""

#Input and Output example
"""
Example Input
Input 1:

 "A"
Input 2:

 "AB"


Example Output
Output 1:

 1
Output 2:

 28


Example Explanation
Explanation 1:

 A -> 1
Explanation 2:

A  -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
"""
class Solution:
	# @param A : string
	# @return an integer
	def titleToNumber(self, A):
        n=len(A)
        j=n-1
        res=0
        for i in range(n):
            x=ord(A[i])-ord('A')+1
            res+=(pow(26,j)*x)
            j-=1
        return res 
