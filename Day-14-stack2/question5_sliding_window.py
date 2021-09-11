from heapq import *
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        heap=[]
        for i in range(k):
            heappush(heap,(-nums[i],i))
        res=[-heap[0][0]]
        
        for i in range(k,len(nums)):
            heappush(heap,(-nums[i],i))
           
            res.append(self.get_max(heap,i-k+1))
            
        return res
        
        
    def get_max(self,heap,start):
        while True:
        
            val,index=heap[0]
            if index>=start:

                return -val

            heappop(heap)

        