class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        count=0
        
        def merge(left,right):
            nonlocal count
            # print(left,right)
            
            i=j=0
            
            while i<len(left) and j<len(right):
                
                if left[i]<=2*right[j]:
                    i+=1
                else:
                    count+=len(left)-i
                    # print(left[i],right[j])
                    j+=1
                    
                    
                    
            
            
            
            
            return sorted(left+right)
        
        
        def mergesort(arr):
            
            if len(arr)<=1:
                return arr
            
            return merge(mergesort(arr[:len(arr)//2]),mergesort(arr[(len(arr)//2):]))
        
        mergesort(nums)
        
        return count