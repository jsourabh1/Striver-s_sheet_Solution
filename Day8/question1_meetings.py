#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        
        
        arr=[]
        
        for i in range(n):
            arr.append([start[i],end[i]])
            
        arr.sort(key=lambda x: x[1])
        
        ans=1
        limit=arr[0][1]
        
        for i in arr:
            
            if i[0]>limit:
                ans+=1
                limit=i[1]
        return ans