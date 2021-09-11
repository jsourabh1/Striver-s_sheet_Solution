from collections import defaultdict
class Solution:
    def romanToInt(self, S: str) -> int:
        mp=defaultdict(lambda:0)
        mp['I'] = 1
        mp['V'] = 5
        mp['X'] = 10
        mp['L'] = 50
        mp['C'] = 100
        mp['D'] = 500
        mp['M'] = 1000
        
        n=len(S)
        i=0
        count=0
        while i<n:
            
            if i+1<n and mp[S[i]]<mp[S[i+1]]:
               
               count+=(mp[S[i+1]]-mp[S[i]])
               i+=1
               
            else:
                count+=mp[S[i]]
                
            i+=1
            
        return count
        