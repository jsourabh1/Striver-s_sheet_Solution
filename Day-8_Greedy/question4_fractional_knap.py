class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        
        arr.sort()
        dep.sort()
        res=1
        ans=1
        
        start=1
        start1=0
        
        while start<len(arr) and start1<len(dep):
            
            if arr[start]<=dep[start1]:
                ans+=1
                start+=1
            
            elif arr[start]>dep[start1]:
                ans-=1
                start1+=1
            
            
            
            res=max(res,ans)
            
        return res