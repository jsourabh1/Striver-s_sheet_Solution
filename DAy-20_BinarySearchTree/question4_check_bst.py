# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math 
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        
        def isbst(root,min,max):
            
            if root is None:
                return True
            
            if root.val>=max or root.val<=min:
                return False
            
            return isbst(root.left,min,root.val) and isbst(root.right,root.val,max)
        
        return isbst(root,-math.inf,math.inf)
        
        
        