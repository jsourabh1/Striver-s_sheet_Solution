class Solution:
    def trap(self, arr: List[int]) -> int:
        
        if len(arr)==0:
            return 0
        
        n=len(arr)
        
        maxl=[]
        maxl.append(arr[0])
        maxr=[0]*n
        maxr[-1]=arr[-1]
        
        for i in range(1,n):
            
            if maxl[i-1]<arr[i]:
                maxl.append(arr[i])
            else:
                maxl.append(maxl[i-1])
        
                
        for i in range(n-2,-1,-1):
            
            
            if maxr[i+1]<arr[i]:
                maxr[i]=arr[i]
            else:
                maxr[i]=maxr[i+1]
                
        count=0
        
        
        for i in range(n):
            
            x=min(maxl[i],maxr[i])-arr[i]
            
            if x>0:
                count+=x
                
        return count
         