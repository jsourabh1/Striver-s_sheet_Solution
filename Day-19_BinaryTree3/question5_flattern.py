# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if not root:
            return None
        
        if root.left:
            self.flatten(root.left)

            temp=root.right
            root.right=root.left
            root.left=None
            
            first=root.right
            
            while first.right:
                first=first.right
                
            first.right=temp
            # root.right.right=temp
        
        self.flatten(root.right)
        