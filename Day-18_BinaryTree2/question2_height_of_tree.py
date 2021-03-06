class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        
        if not root:
            return 0
            
        return 1+max(self.height(root.left),self.height(root.right))
