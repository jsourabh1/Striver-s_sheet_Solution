"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        queue=[]
        queue.append(root)
        
        while queue:
            
            count=len(queue)
            
            while count:
                node=queue.pop(0)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    
                    queue.append(node.right)
                    
                if count-1==0:
                    node.next=None
                else:
                    node.next=queue[0]
                count-=1
                    
        return root


class Solution:
    def connect(self, root):
        temp=root
        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next
        return temp