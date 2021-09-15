
class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        
        a=sorted(a)
        b=sorted(b)
        
        if len(a)!=len(b):
            return False
        for i in range(len(a)):
            
            if a[i]!=b[i]:
                return False
                
        return True