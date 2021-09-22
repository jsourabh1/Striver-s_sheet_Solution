def findSpiral(root):
    # Code here
    
    if not root:
        return []
    ans=[]
    queue=[]
    count=0
    queue.append(root)
    
    while queue:
        
        if count%2==0:
            
            for i in queue[::-1]:
                ans.append(i.data)
            
        else:
            for i in queue:
                ans.append(i.data)
        n=len(queue)
        count+=1
        
        while n:
            
            node=queue.pop(0)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
            n-=1
            
    return ans

#level order traversal using recursion 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def height(root):
    
    if not root:
        return 0
    left=height(root.left)
    right=height(root.right)
    
    return 1+max(left,right)
def printlevel(root,level,ans):
    
    if not root:
        return ans
    
    if level==1:
        ans.append(root.val)
        return ans 
    printlevel(root.left,level-1,ans)
    printlevel(root.right,level-1,ans)
    
    return ans
    
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        n=height(root)
        ans=[]
        
        for i in range(1,n+1):
            
            ans.append(printlevel(root,i,[]))
            
        return ans[::-1]
        
        
                    
                
            
        
            
