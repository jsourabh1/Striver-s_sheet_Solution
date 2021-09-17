
from collections import defaultdict
class Solution:
    def bottomView(self, root):
        
        
        dict_1=defaultdict(dict)
        
        
        
        def helper(row,col,root):
            nonlocal dict_1
            if not root:
                return 
            if  row not in dict_1[col]:
                dict_1[col][row]=[]
          
            
            dict_1[col][row].append(root.data)
            
            helper(row+1,col-1,root.left)
            helper(row+1,col+1,root.right)
        helper(0,0,root)
        # print(dict_1)
        
        res=[]
        
        for i in sorted(dict_1.keys()):
            res.append(dict_1[i][sorted(dict_1[i].keys())[-1]][-1])
            
            
        return res
                    