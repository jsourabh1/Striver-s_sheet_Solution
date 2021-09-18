class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def postorder(root):


	if not root:
		return 

	postorder(root.left)
	postorder(root.right)
	print(root.data,end=" ")


def postorder2(root):


	if not root:
		return

	stack=[]

	current=root
	while True:
		# print(stack)
		while current:

			if current.right:

				stack.append(current.right)

			stack.append(current)
			current=current.left



		current=stack.pop()

		if current.right is not None and stack and stack[-1]==current.right:
			# print("T")
			stack.pop()

			stack.append(current)

			current=current.right

		else:

			print(current.data,end=" ")

			current=None

		if not stack:
			break


def postorder3(root):

	if not root:
		return 


	visited=set()

	current=root

	while current and current not in visited:

		if current.left and current.left not in visited:
			current=current.left

		elif current.right and current.right not in visited:

			current=current.right

		else:

			print(current.data,end=" ")

			visited.add(current)
			current=root





root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)


postorder(root)

print()

postorder2(root)

print()

postorder3(root)

print()
