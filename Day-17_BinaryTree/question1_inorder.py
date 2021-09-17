class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# With recursion

def inorder(root):
    if not root:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


# With stack and without recursion

def inorder2(root):
    if not root:
        return

    queue = []

    ans = []

    while queue or root:

        if root:

            queue.append(root)
            root = root.left

        else:

            ans.append(queue[-1].data)

            root = queue.pop().right

    print(ans)


# Without recursion and stack only iterative with space O(1)


def inorder3(root):
    if not root:
        return

    current = root


    while current is not None:
    
        if current.left is None:
            print(current.data, end=" ")
            current = current.right

        else:
            pre = current.left
            while (pre.right is not None) and (pre.right is not current):
                pre = pre.right

            if pre.right is None:
                pre.right = current
                current = current.left
            else:
                print(current.data,end=" ")
                pre.right = None
                current = current.right

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)

inorder(root)

print()

inorder2(root)
print()

inorder3(root)
