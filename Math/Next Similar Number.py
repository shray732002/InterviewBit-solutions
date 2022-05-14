#Problem Description
"""
Given a number A in a form of string.

You have to find the smallest number that has same set of digits as A and is greater than A.

If A is the greatest possible number with its set of digits, then return -1.
"""
#Example Input and Output
"""
Example Input
Input 1:

 A = "218765"
Input 2:

 A = "4321"


Example Output
Output 1:

 "251678"
Output 2:

 "-1"
 
 Explanation 1:

 The smallest number greater then 218765 with same set of digits is 251678.
Explanation 2:

 The given number is the largest possible number with given set of digits so we will return -1.
"""
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        lst=[]
        for i in range(len(A)):
            lst.append(A[i])
            
        lst3=lst[:]   
        
        lst3.sort(reverse=True)
        
        if lst==lst3:
            return -1
        else:
            indexele=-1
            index=-1
            for i in range(len(A)-2,-1,-1):
                lst1=[]
                lst1= lst[i:]
                
                lst2=lst1[:]
                
                lst2.sort(reverse=True)
                          
                if lst1!=lst2:
                    index=i
                    indexele=lst[i]
                    break
            
            
            lst1.sort()
            countele=lst1.count(indexele)
            index1=lst1.index(indexele)+countele
            lst4=[]
            lst4.append(lst1[index1])
            lst1.pop(index1)
            
            for i in range(len(lst1)):
                lst4.append(lst1[i])
            lst[index:]=lst4   
            str1=''.join(lst)
            return str1    
