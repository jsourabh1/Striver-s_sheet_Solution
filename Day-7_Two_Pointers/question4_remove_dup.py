class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        N=len(arr)
        
        if N==0 or N==1:
            return N
        index=0
        
        for i in range(N-1):
            
            if arr[i]!=arr[i+1]:
                
                arr[index]=arr[i]
                index+=1
        arr[index]=arr[N-1]
        index+=1
        return index
        
        
        