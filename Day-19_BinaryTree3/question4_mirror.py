class Solution:
    # return true/false denoting whether the tree is Symmetric or not
    def isSymmetric(self, root):
        # Your Code Here
        
        if not root:
            return True
            
       
        def helper(root1,root2):
            if not root1 and not root2:
                return True
            
            if (not root1 and root2) or (not root2 and root1):
                return False
                
            if root1.data !=root2.data:
                return False
                
            left=helper(root1.left,root2.right)
            right=helper(root1.right,root2.left)
            
            return left and right
        
        return helper(root.left,root.right)