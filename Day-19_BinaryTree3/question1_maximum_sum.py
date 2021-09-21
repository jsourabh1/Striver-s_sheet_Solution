# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ans=-float("inf")
        
        def helper(root):
            
            nonlocal ans 
            
            if not root:
                return 0
            
            left=helper(root.left)

            right=helper(root.right)
            
            ans=max(ans,root.val+left+right,root.val,root.val+max(left,right))
            
            return max(root.val,root.val+max(left,right))
        
        helper(root)
        return ans