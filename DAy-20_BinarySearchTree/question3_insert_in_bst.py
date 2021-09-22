#User function Template for python3


#Function to insert a node in a BST. 
def insert(root, val):

    if not root:
        return Node(val)
        
    if root.data==val:
        return root
        
   
    if root.data<val:
        root.right=insert(root.right,val)
    else:
        root.left=insert(root.left,val)
            
    return root
  