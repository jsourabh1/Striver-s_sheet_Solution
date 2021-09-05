from itertools import permutations
class Solution:
    def find_permutation(self, S):
        
        ans=[]
        for i in list(permutations(S)):
            
            ans.append("".join(i))
        return sorted(ans)
        