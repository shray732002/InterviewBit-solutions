#Problem Description
"""
Given a positive integer A, return its corresponding column title as appear in an Excel sheet.
"""
#Example Input and Output
"""
Example Input
Input 1:

 A = 1
Input 2:

 A = 28


Example Output
Output 1:

 "A"
Output 2:

 "AB"


Example Explanation
Explanation 1:

 1 -> A
Explanation 2:

1 -> A
2 -> B
3 -> C
...
26 -> Z
27 -> AA
28 -> AB 
"""
class Solution:
	# @param A : integer
	# @return a strings
	def convertToTitle(self, A):
        lst=[]
        
        while(A>0):
            a=A%26
            if(a==0):
                lst.append('Z')
                A=int(A/26)-1
            else:
                a+=64
                lst.append(chr(a))
                A=int(A/26) 
        lst.reverse() 
        str1=''.join(lst)
        return str1
