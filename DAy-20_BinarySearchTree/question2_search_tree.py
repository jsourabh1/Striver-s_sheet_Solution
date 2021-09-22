x# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        ans=None
        def helper(root,val):
            nonlocal ans
            if not root:
                return ans
            
            if root.val==val:
                ans=root
                return 
            
            helper(root.left,val)
            helper(root.right,val)
        helper(root,val)
        return ans
            
            