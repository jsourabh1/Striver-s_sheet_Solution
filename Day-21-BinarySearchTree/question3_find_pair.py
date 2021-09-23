'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
from collections import defaultdict

class Solution:
    # root : the root Node of the given BST
    # target : the target sum
    def isPairPresent(self,root, k): 
        # code here.
        dict_1=defaultdict(lambda:0)
        
        def helper(root):
            nonlocal k,dict_1
            
            if not root:
                return False
            
            
            if dict_1[root.data]==1:
                return True
            dict_1[k-root.data]=1
            
            return helper(root.left) or helper(root.right)
        if helper(root):
            return 1
        return 0
        