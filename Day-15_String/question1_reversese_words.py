class Solution:
    def reverseWords(self, s: str) -> str:
        
        
        words=s.split()
        n=len(words)
        for i in range(len(words)//2):
            
            words[i],words[n-1-i]=words[n-1-i],words[i]
            
            
        return  " ".join(words)
    
    
            
        