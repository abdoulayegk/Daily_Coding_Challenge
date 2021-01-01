class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sorted_array(arr):
    if not arr:
        return None
    mid = len(arr)//2
    # make the mid value as root
    root = Node(arr[mid])
    # do the same for the left and right subtree recursivly
    root.left = sorted_array(arr[:mid])
    root.right = sorted_array(arr[mid+1:])
    return root


def preOrder(node):
    if not node:
        return
    print(node.data)
    preOrder(node.left)
    preOrder(node.right)


arr = [1, 2, 3, 4, 5, 6, 7]
root = sorted_array(arr)
print("PreOrder Traversal of constructed BST ", preOrder(root))
