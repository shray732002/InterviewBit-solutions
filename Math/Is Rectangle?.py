# Problem Description
"""
Given four positive integers A, B, C, D, determine if there’s a rectangle such that the lengths of its sides are A, B, C and D (in any order).

If any such rectangle exist return 1 else return 0.
"""
# Example Input and output
"""
Example Input
Input 1:

 A = 1
 B = 1
 C = 2
 D = 2
Input 2:

 A = 1
 B = 2
 C = 3
 D = 4


Example Output
Output 1:

 1
Output 2:

 0
"""
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        lst=[]
        lst.append(A)
        lst.append(B)
        lst.append(C)
        lst.append(D)
        lst1=[]
        flag=0
        for i in lst:
            if i not in lst1:
                lst1.append(i)
        for i in lst1:
            if(lst.count(i)==2 or lst.count(i)==4):
                flag=1
            else:
                flag=0
                break
        if flag==1:
            return 1
        else:
            return 0
