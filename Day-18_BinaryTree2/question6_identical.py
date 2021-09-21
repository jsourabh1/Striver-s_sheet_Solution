
class Solution:
    #Function to check if two trees are identical.
    def isIdentical(self,root1, root2):
        # Code here
        if not root1 and not root2:
            return True
        
        if (not root1 and root2) or (not root2 and root1):
            return False
            
        if root1.data !=root2.data:
            return False
            
        left=self.isIdentical(root1.left,root2.left)
        right=self.isIdentical(root1.right,root2.right)
        
        return left and right