class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



#with recursion 
def preorder(root):

	if not root:
		return 

	print(root.data,end=" ")
	preorder(root.left)
	preorder(root.right)



#without recrursion
def preorder2(root):


	if not root:
		return 


	queue=[]
	ans=[]

	while queue or root:

		if root:

			queue.append(root)
			ans.append(root.data)

			root=root.left

		else:

			node=queue.pop()
			root=node.right


	print(*ans)

#without recrursion and queue





root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)

preorder(root)

print()

preorder2(root)

