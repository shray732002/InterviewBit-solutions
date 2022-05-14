#Problem Description
"""
Given a set of digits (A) in sorted order, find how many numbers of length B are possible whose value is less than number C.
NOTE: All numbers can only have digits from the given set.  

Examples:

Input:
  0 1 5

  1

  2

Output:

  2 (0 and 1 are possible)  


Input:
  0 1 2 5

  2

  21

Output:
  5 (10, 11, 12, 15, 20 are possible)
"""
def lowernumbers(A,lst,b):
    count=0
    for i in range(len(A)):
        if(A[i]<b):
            count+=1
    return count
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @param C : integer
	# @return an integer
  def solve(self, A, B, C):
    if len(A)==0:
        return 0
    if pow(10,B-1)>C:
        return 0
    elif pow(10,B)<=C:
        if(B==1):
            return len(A)
        else:
         count_0=A.count(0)
         n=len(A)
         return (n-count_0)*pow(n,B-1)
    else:
        lst=[]
        while(C!=0):
            lst.append(C%10)
            C=C//10
        lst.reverse()
        rank=0
        N=len(lst)
        if(B == 1):
            return lowernumbers(A,lst,lst[0])
               
        for i in range(N):
            pos=1
            if(i==0):
                pos*=(lowernumbers(A,lst,lst[0])-A.count(0))
                pos*=pow(len(A),B-1)
                
            else:
                pos*=(lowernumbers(A,lst,lst[0]))
                pos*=pow(len(A),len(lst)-1)
              
            rank+=pos
            if (lst[0] not in A):
                return rank
            lst.pop(0)

        return rank
