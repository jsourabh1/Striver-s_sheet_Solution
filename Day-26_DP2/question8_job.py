class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        
        job=sorted(zip(startTime,endTime,profit),key=lambda x:x[1])
        
        dp=[[0,0]]  #[[endTime,profit]]
        
        
        for a,b,c in job:
            
            index=bisect.bisect(dp,[a+1])-1
            
            if dp[index][1]+c>dp[-1][1]:
                dp.append([b,dp[index][1]+c])
            print(dp)
                
        return dp[-1][1]