# Your task is to complete this function

'''

class Node:
def __init__(self, data):
    self.data = data
    self.next = None

'''


class Solution:

#Function to rotate a linked list.
def rotate(self, head, k):
    
    
    if not head:
        return head
    
    current=head
    length=0
    while current.next:
        length+=1
        current=current.next
    length+=1
    # print(length) 
    k=k%length
    
    if k :
        last=current
        prev=None
        curr=head
        for i in range(k):
            
            prev=curr
            curr=curr.next
        # print(prev.val,curr.val)
        last.next=head
        prev.next=None
        return curr
        
    return head
        