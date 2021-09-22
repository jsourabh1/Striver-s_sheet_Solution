def solve(root,key):

	if not root:
		return

	floor=-1
	ceil=-1

	while root:

		if root.data==val:
			floor=root.data
			ceil=root.data
			break

		if root.data<key:
			floor=root.data
			root=root.right

		else:
			ceil=root.data
			root=root.left

	print(floor,ceil)