class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            
            if nums[0]==1:
                return 1
            else:
                return  0
            
        
        ans=0
        count=0
        for i in range(len(nums)):
            
            if nums[i]!=1:
                count=0
            else:
                count+=1
                ans=max(ans,count)
            # print(index)
            
        return ans
                