# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], K: int) -> int:
        
        
        ans=-1
        count=0
        def solve(root):
            nonlocal K,ans,count
            if not root:
                return -1
                
            if root.left:
                
                solve(root.left)
            # print(count,K)
            count+=1
            if count==K:
                ans=root.val
                
            if root.right:
                
                solve(root.right)
                
            # count+=1
            
            
            
                
            return -1
        solve(root)
        return ans
        