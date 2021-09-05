
class Solution:
    
    #Function to return a list of indexes denoting the required 
    #combinations whose sum is equal to given number.
    def combinationalSum(self,arr, target):
    
        temp=[]
        ans=[]
        
        arr=sorted(list(set(arr)))
        
        def helper(temp,index,target):
            nonlocal arr,ans 
            if target==0:
                
                ans.append(list(temp))
                # print(temp)
                return 
            
            for i in range(index,len(arr)):
                
                if target-arr[i]>=0:
                    
                    temp.append(arr[i])
                    
                    helper(temp,i,target-arr[i])
                    temp.remove(arr[i])
        helper(temp,0,target)
        return ans