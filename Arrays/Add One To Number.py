#Problem Description
"""
Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.
NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. For example: 
for this problem, following are some good questions to ask :

Q : Can the input have 0's before the most significant digit. Or in other words, is 0 1 2 3 a valid input?
A : For the purpose of this question, YES
Q : Can the output have 0's before the most significant digit? Or in other words, is 0 1 2 4 a valid output?
A : For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.
"""
#Example Input and Output
"""
Example Input
Input 1:

[1, 2, 3]


Example Output
Output 1:

[1, 2, 4]


Example Explanation
Explanation 1:

Given vector is [1, 2, 3].
The returned vector should be [1, 2, 4] as 123 + 1 = 124.
"""
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        n=len(A)
        A[n-1]+=1
        carry=A[n-1]//10 
        A[n-1]=A[n-1]%10
        
        for i in range(n-2,-1,-1):
            A[i]+=carry
            carry=A[i]//10
            A[i]=A[i]%10
            
        if(carry):
            A.insert(0,carry)
        for i in range(len(A)):
            if (A[0] != 0):
              return A
            if (A[0] == 0):
              A.pop(0)
        return A
