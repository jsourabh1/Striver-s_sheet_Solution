"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        #using hashmap 
        
        dict_1={}
        
        current=head
        
        clone=None
        
        
        while current:
            
            clone=Node(current.val)
            dict_1[current]=clone
            current=current.next
            
        dict_1[None]=None
        current=head
        # print(dict_1)
        
        while current:
            
            clone=dict_1[current]
            clone.next=dict_1[current.next]
            clone.random=dict_1[current.random]
            current=current.next
            
        return dict_1[head]
        
        


# without extra space

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        
        current=head
    
       
        prev=None
        while current:
            
            temp=current.next
            
            newnode=Node(current.val)
            current.next=newnode
            newnode.next=temp
           
            current=temp
            
        current=head
        
        while current:
            if current.random is not None:
                current.next.random=current.random.next
            current=current.next.next
            
        copy=head1=Node(0)
        current=head
        while current:
            
            temp=current.next.next
            head1.next=current.next
            head1=head1.next
            current.next=temp
            current=current.next
            
        return copy.next
            
            
            
        
    
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        