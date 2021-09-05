class Solution:
    def isSubsetSum (self, N, arr, sum):
        
        def solve(i,j):
            nonlocal arr
            if i==0 and j==0:
                return True
            
            elif j==0:
                return True
                
            elif i==0:
                
                return False
                
            elif arr[i-1]<=j:
                
                return solve(i-1,j-arr[i-1]) or solve(i-1,j)
                
            else:
                
                return solve(i-1,j)
   
        return solve(N,sum) 