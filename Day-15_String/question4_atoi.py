
# question practise link:- https://practice.geeksforgeeks.org/problems/implement-atoi/1

def atoi(self,string):
    
    ans=0
    first=1
    for i in string[::-1]:
        
        if i=="-":
            ans=ans-2*ans
        elif not  i.isnumeric():
            return -1
        else:
            ans+=int(i)*first
            first*=10
    return ans
