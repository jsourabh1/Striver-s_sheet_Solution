class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        fact=1
        number=[]
        
        for i in range(1,n):
            fact=fact*i
            number.append(i)
        # print(fact)
        number.append(n)
        
        k=k-1
        ans=""
        while True:
            
            ans+=str(number[int(k//fact)])
            # print(ans)
            number.remove(number[int(k//fact)])
            # print(number)
            if len(number)==0:
                break
                
            k%=fact
            fact/=len(number)
            # print(fact)
            
        return ans
            
            
        