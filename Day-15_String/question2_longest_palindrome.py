#User function Template for python3

class Solution:
    def longestPalin(self, s):
        
        maxx=0
        ans=""
        
        t=[[False]*(len(s)) for i in range(len(s))]
        
        for i in range(len(s)):
            
            t[i][i]=True
            
        for i in range(len(s)-1,-1,-1):
		
            for j in range(i+1,len(s)):
                if s[i]==s[j]:


                    if j-i==1 or t[i+1][j-1]:

                        t[i][j]=True

                        if len(ans)<=j-i+1:

                            maxx=j-i+1
                            ans=s[i:j+1]
                            
        return ans if ans else s[0]
        