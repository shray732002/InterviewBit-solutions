#Problem Description
"""
Determine whether an integer is a palindrome. Do this without extra space.

A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed. Negative numbers are not palindromic.
"""
#Example
"""
Example :

Input : 12121
Output : 1


Input : 123
Output : 0
"""
class Solution:
	# @param A : integer
	# @return an integer
	def isPalindrome(self, A):
        if A < 0: return 0
        if A < 10: return 1
        j=0
        p=A
        
        while(p>0):
            j+=1
            p=int(p/10)
        res=0
        j-=1
        s=A
        while(j>=0):
            res+=((s%10)*pow(10,j))
            s=int(s/10)
            j-=1
        if(res==A):
            return 1
        else:
            return 0   
