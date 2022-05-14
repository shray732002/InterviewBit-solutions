#Problem Description
"""
You are given an integer N and the task is to reverse the digits of the given integer. Return 0 if the result overflows and does not fit in a 32 bit signed integer

Look at the example for clarification.
"""
#Example Input and output
"""
Example Input
Input 1:

 x = 123


Input 2:

 x = -123


Example Output
Output 1:

 321


Ouput 2:

 -321


Example Explanation
 If the given integer is negative like -123 the output is also negative -321.
"""
class Solution:
	# @param A : integer
	# @return an integer
	def reverse(self, A):
            p=abs(A)
            j=0
            while(p>0):
                j+=1
                p=int(p/10)
            res=0
            j-=1
            s=abs(A)
            while(j>=0):
                res+=((s%10)*pow(10,j))
                if(res>2147483647):
                    return 0
                s=int(s/10)
                j-=1
            if(A<0):
                return -1*res
            else:
                return res
