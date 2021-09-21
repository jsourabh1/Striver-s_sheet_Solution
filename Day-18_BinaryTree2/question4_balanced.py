class Solution:
    def isBalanced(self,root):
    
        #add code here
        ans=True
        
        def helper(root):
            nonlocal ans
            if not root:
                return 0
                
            left=helper(root.left)
            right=helper(root.right)
            
            if abs(left-right)>1:
                ans=False
                
            return 1+(max(left,right))
        helper(root)
        return ans
            