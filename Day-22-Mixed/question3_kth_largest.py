#User function Template for python3
from heapq import *
class Solution:
    def kthLargest(self, k, arr, n):
        # code here
        
        heap=[]
        heapify(heap)
        
        ans=[]
        
        for i in range(n):
            
            if len(heap)<k:
                heappush(heap,arr[i])
                
            else:
                
                if arr[i]>heap[0]:
                    heappop(heap)
                    heappush(heap,arr[i])
                    
            if len(heap)<k:
                ans.append(-1)
                
            else:
                ans.append(heap[0])
                
        return ans
            