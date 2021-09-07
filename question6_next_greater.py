
class Solution:
    def nextLargerElement(self,arr,n):
        
        stack=[]
        ans=[-1]*n
        for i in range(n-1,-1,-1):
            
            while stack and stack[-1]<arr[i]:
                stack.pop()
                
            if not stack:
                ans[i]=-1
            else:
                ans[i]=stack[-1]
            stack.append(arr[i])
                
        return ans
