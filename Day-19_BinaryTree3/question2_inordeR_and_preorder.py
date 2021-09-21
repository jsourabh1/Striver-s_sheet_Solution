# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, post: List[int], In: List[int]) -> Optional[TreeNode]:
        
        index=0
    
    
        def helper(n,post,start,end):
            nonlocal index
            if start>end:
                return None
                
            node=TreeNode(post[index])
            index+=1
            if start==end:
                return node
                
            # 
            temp=n.index(post[index-1])
            # print(temp)
            
            node.left=helper(n,post,start,temp-1)
            node.right=helper(n,post,temp+1,end)
            
            return node
        return helper(In,post,0,len(In)-1)
        