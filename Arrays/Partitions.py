#Problem Description
"""
You are given a 1D integer array B containing A integers.

Count the number of ways to split all the elements of the array into 3 contiguous parts so that the sum of elements in each part is the same.

Such that : sum(B[1],..B[i]) = sum(B[i+1],...B[j]) = sum(B[j+1],...B[n]) 
"""
#Example Input and Output
"""
Example Input
Input 1:

 A = 5
 B = [1, 2, 3, 0, 3]
Input 2:

 A = 4
 B = [0, 1, -1, 0]


Example Output
Output 1:

 2
Output 2:

 1


Example Explanation
Explanation 1:

 There are no 2 ways to make partitions -
 1. (1,2)+(3)+(0,3).
 2. (1,2)+(3,0)+(3).
Explanation 2:

 There is only 1 way to make partition -
 1. (0)+(-1,1)+(0).
"""
def fact(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    return factorial    
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n=len(B)
        res_sum=sum(B)/3
        prefixsum=[]
        sumv=0
        for i in range(n):
            sumv+=B[i]
            prefixsum.append(sumv)
        if res_sum==0:
            freq=prefixsum.count(0)-1
            fact_num=fact(freq)
            fact_den=2*fact(freq-2)
            return fact_num//fact_den
        else:
            idx1,idx2,idx3=0,0,0
            for i in range(n):
                if(prefixsum[i]==3*res_sum):
                    idx3=i
                elif(prefixsum[i]==2*res_sum):
                    idx2=i 
                elif(prefixsum[i]==res_sum):
                    idx1=i 
            if((idx1<idx2 and idx2<idx3)==0):
                return 0              
            count=0
            for i in range(n):
                if(prefixsum[i]==res_sum):
                    lst2=prefixsum[i+1:]
                    count+=lst2.count(2*res_sum)
            return count   
