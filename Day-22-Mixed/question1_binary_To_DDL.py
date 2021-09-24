
'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''
class solve:
    
    def __init__(self):
        
        self.head=self.tail=None
        
        
    def Solve(self,root):
        
        if not root:
            return self.head
            
            
        self.Solve(root.left)
        
        node=root
        
        if self.head is None:
            self.head=node
            
        else:
            self.tail.right=node
            node.left=self.tail
            
        self.tail=node
        
        self.Solve(root.right)
        return self.head
#Function to convert a binary tree to doubly linked list.
class Solution:
    def bToDLL(self,root):
        
        
        obj=solve()
        
        return obj.Solve(root)
