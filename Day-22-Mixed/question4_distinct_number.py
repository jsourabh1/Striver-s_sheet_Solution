from collections import defaultdict
class Solution:
    def countDistinct(self, A, N, K):
        # Code here
        
        map=defaultdict(lambda:0)
        
        count=0
        
        for i in range(K):
            
            if map[arr[i]]==0:
                count+=1
            map[arr[i]]+=1
        ans=[count]        
        for i in range(K,N):
           
            # print(map.items(),arr[i-K])
            if map[arr[i-K]]>1:
                map[arr[i-K]]-=1
                
            else:
                count-=1
                map[arr[i-K]]-=1
            # print(count)
            if map[arr[i]]>=1:
                
                map[arr[i]]+=1
                
            else:
                map[arr[i]]+=1
                count+=1
            ans.append(count)
            
        return ans
        