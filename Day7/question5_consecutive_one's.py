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
                

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        
        start=end=ans=count=0
        
        while end<len(nums):
            
            if  nums[end]==1:
                end+=1
                ans=max(ans,end-start)
                
            else:
                
                if count<k:
                    end+=1
                    count+=1
                    
                    ans=max(ans,end-start)
                else:
                    
                    while start<=end and count>=k:
                        
                        if nums[start]==0:
                            count-=1
                            
                        start+=1
                        
        return ans
                    
        