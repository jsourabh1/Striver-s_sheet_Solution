class Solution:
    def coinChange(self, coins: List[int], V: int) -> int:
        
        M=len(coins)
        
        t=[[-1]*(V+1) for i in range(M+1)]
		
# 		intialzation?\
        # print(t)
        
        # for i in range(1,V+1):
        #     # print(i)
        #     if i%coins[0]==0:
                
        #         t[1][i]=i//coins[0]
        #     else:
        #         t[1][i]=float("inf")-1
                
        for i in range(M+1):
            
            for j in range(V+1):
                
                if i==j==0:
                    t[i][j]=float("inf")-1
                    
                elif i==0:
                    t[i][j]=float("inf")-1
                elif j==0:
                    
                    t[i][j]=0
                    
                elif coins[i-1]<=j:
                    
                    t[i][j]=min(1+t[i][j-coins[i-1]],t[i-1][j])
                else:
                    t[i][j]=t[i-1][j]
                    
        if t[M][V]!=float("inf")-1:
            return t[M][V]
        return -1