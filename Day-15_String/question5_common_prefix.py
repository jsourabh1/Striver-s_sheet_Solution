
class Solution:
    def longestCommonPrefix(self, arr, n):
        
        string=""
        m=float("inf")
        for i in range(n):
            
            m=min(m,len(arr[i]))
            
            
        for i in range(m):
            ans=True
            temp=arr[0][i]
            for j in range(1,n):
                
                if temp!=arr[j][i]:
                    ans=False
                    break
            if not ans:
                break
            string+=temp
            
        if not string:
            return -1
        return string
            
                