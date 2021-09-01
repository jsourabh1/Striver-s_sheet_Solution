# withour extra space O(n)


class Solution:
    def sort012(self,arr,n):
        ans=[]
        index=0
        
        for i in range(n):
            if arr[i]==2:
                ans.append(arr[i])
                
            elif arr[i]==1:
                ans.insert(index,arr[i])
                index+=1
            else:
                ans.insert(0,arr[i])
                index+=1

from collections import Counter
class Solution:
    def sort012(self,arr,n):
        
        dict_1=Counter(arr)
        count1=dict_1[1]
        count2=dict_1[2]
        count0=dict_1[0]
        for i in range(n):
            
            if count0>0:
                arr[i]=0
                count0-=1
            elif count1>0:
                arr[i]=1
                count1-=1
            else:
                arr[i]=2
                count2-=1