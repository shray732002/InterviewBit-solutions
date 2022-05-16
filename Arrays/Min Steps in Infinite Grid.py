#Problem Description
"""
You are in an infinite 2D grid where you can move in any of the 8 directions

 (x,y) to 
    (x-1, y-1), 
    (x-1, y)  , 
    (x-1, y+1), 
    (x  , y-1),
    (x  , y+1), 
    (x+1, y-1), 
    (x+1, y)  , 
    (x+1, y+1) 
You are given a sequence of points and the order in which you need to cover the points.. Give the minimum number of steps in which you can achieve it. You start from the first point.

NOTE: This question is intentionally left slightly vague. Clarify the question by trying out a few cases in the “See Expected Output” section.
"""
#Example Input and Output
"""
Example Input
Input 1:

 A = [0, 1, 1]
 B = [0, 1, 2]


Example Output
Output 1:

 2


Example Explanation
Explanation 1:

 Given three points are: (0, 0), (1, 1) and (1, 2).
 It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
"""
class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
	def coverPoints(self, A, B):
        count=0
        for i in range(len(A)-1):
            
            if(B[i]==B[i+1]):
                count+=abs(A[i+1]-A[i])
            elif(A[i]==A[i+1]):
                count+=abs(B[i+1]-B[i])
            elif(abs(A[i+1]-A[i])<=abs(B[i+1]-B[i])):
                p=abs(A[i+1]-A[i])
                count+=p
                if(B[i]<B[i+1]):
                    newBi=B[i]+p
                    count+=(B[i+1]-newBi)
                else:
                    newBi=B[i]-p    
                    count+=(newBi-B[i+1])
            elif(abs(A[i+1]-A[i])>abs(B[i+1]-B[i])):
                p=abs(B[i+1]-B[i])
                count+=p
                if(A[i]<A[i+1]):
                    newAi=A[i]+p
                    count+=(A[i+1]-newAi)
                else:
                     newAi=A[i]-p
                     count+=(newAi-A[i+1])
        return count    
