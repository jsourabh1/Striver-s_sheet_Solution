class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n):
        
        if n==0:
            return False
        
        if (n&(n-1))==0:
            return True
        return False