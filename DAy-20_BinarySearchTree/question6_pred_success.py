

# Python program to find predecessor and successor in a BST
 
# A BST node
class Node:
 
    # Constructor to create a new node
    def __init__(self, key):
        self.key  = key
        self.left = None
        self.right = None
 
def solve(root,val):


	def helper(root,val):

		if not root:
			return 

		if root.key==val:

			print("The predecessor of the give node")

			temp=root.left
			while temp and temp.right:
				temp=temp.right
			print(temp.key)

			print("The successor of the given node")

			temp=root.right

			while temp and temp.left:
				temp=temp.left
			print(temp.key)


		if root.key<val:
			helper(root.right,val)

		else:
			helper(root.left,val)

	helper(root,val)

def insert(node , key):
    if node is None:
        return Node(key)
 
    if key < node.key:
        node.left = insert(node.left, key)
 
    else:
        node.right = insert(node.right, key)
 
    return node
 
 
# Driver program to test above function
key = 65 #Key to be searched in BST
  
""" Let us create following BST
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80
"""
root = None
root = insert(root, 50)
insert(root, 30);
insert(root, 20);
insert(root, 40);
insert(root, 70);
insert(root, 60);
insert(root, 80);
 
# Static variables of the function findPreSuc
# findPreSuc.pre = None
# findPreSuc.suc = None
 
solve(root, 55)

