
class Solution:
    
    #Function to sort the binary array.
    def binSort(self,arr, N): 
        #Your code here
        #No need to print the array
        
        left,right=0,N-1
        
        while left<right:
            
            while arr[left]==0 and left<right:
                left+=1
            while arr[right]==1 and left<right:
                right-=1
                
            if left<right:
                arr[left]=0
                arr[right]=1
                left+=1
                right-=1
                
        return arr