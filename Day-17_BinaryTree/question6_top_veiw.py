# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        
        res=[]
        
        
        dict_1=collections.defaultdict(dict)
        
        
        def recursion(root,row,col,dict_1):
            
            
            if not root:
                return 
            if  row not in dict_1[col]:
                dict_1[col][row]=[]
          
            
            dict_1[col][row].append(root.val)
            
            recursion(root.left,row+1,col-1,dict_1)
            recursion(root.right,row+1,col+1,dict_1)
            
            
        recursion(root,0,0,dict_1)
        print(dict_1)
        for i in sorted(dict_1.keys()):
            temp=[]
            for j in sorted(dict_1[i].keys()):
                   temp+=sorted(dict_1[i][j])
                    
                    
            res.append(temp)
                   
                   
        return res
            
                   