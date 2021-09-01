class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m==1 and n==1:
            return 1
        
        dp=[[-1]*(n+1) for i in range(m+1)]
        def helper(first,second):
            nonlocal m,n,dp
            
            if first==m and second==n:
                return 1
            if first>m or second>n:
                return 0
            if dp[first][second]!=-1:
                return dp[first][second]
            
            dp[first][second]=helper(first+1,second)+helper(first,second+1)
            return dp[first][second]
        
        helper(1,1)
        # print(dp)
        return dp[1][1]
            
print((1,2)==(2,1))