#User function Template for python3
from heapq import *
class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        heap=[]
        heapify(heap)
        
        for i in arr:
            
            heappush(heap,-i)
            
            if len(heap)>k:
                heappop(heap)
                
        return -heap[0]



# full implementation



from heapq import heapify
class Solution:
    
    def Max_heapify(self,arr,index):
        
        
        left=2*index+1
        right=2*index+2
        largest=index
        if left <len(arr) and arr[largest]<arr[left]:
            largest=left
            
        if right<len(arr) and arr[largest]<arr[right]:
            
            largest=right
            
        if largest!=index:
            
            arr[index],arr[largest]=arr[largest],arr[index]
            self.Max_heapify(arr,largest)
        return arr
    
    def extract_max(self,arr):
        maxx=arr[0]
        arr[0],arr[-1]=arr[-1],arr[0]
        arr=arr[:len(arr)-1]
        arr=self.Max_heapify(arr,0)
        return arr
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        for i in range(len(nums)//2,-1,-1):
            nums=self.Max_heapify(nums,i)
        for i in range(k-1):
            nums=self.extract_max(nums)
            
        return nums[0]
        
        