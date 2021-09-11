class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        
        ans=[]
        
        for  i in range(n):
            flag=True
            for j in range(n):
                
                if M[i][j]==1:
                    flag=False
                    break
            if flag:
                ans.append(i)
        if len(ans)>1 or len(ans)==0:
            return -1
        return ans[0]
                
