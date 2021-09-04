class Solution:
    def combinationSum2(self, arr: List[int], target: int) -> List[List[int]]:
        
        temp=[]
        ans=[]
        
        
        arr=sorted(arr)
        def helper(temp,index,target):
            nonlocal arr,ans 
            if target==0:
                
                ans.append(list(temp))
                # print(temp)
                return 
            
            for i in range(index,len(arr)):
                
                if i>index and arr[i]==arr[i-1]:
                    continue
                    
                if target-arr[i]<0:
                    break
                    
                temp.append(arr[i])

                helper(temp,i+1,target-arr[i])
                temp.remove(arr[i])
        helper(temp,0,target)
        return ans
        