# PF 6.9 - Binary Search Tree
# Samuel Marriott 8/03/2026

class BSTNode:
    def __init__(self, value):
        self.value = value  # Node value
        self.left = None  # Pointer to left child
        self.right = None  # Pointer to right child

def insert(root, value):
    if root is None:
        return BSTNode(value)  # Create a new node if the tree is empty

    if value < root.value:
        root.left = insert(root.left, value)  # Insert into the left subtree
    else:
        root.right = insert(root.right, value)  # Insert into the right subtree
    return root

root = None
values = [42, 13, 56, 8, 21, 72]  # Sample values

for val in values:
    root = insert(root, val)  # Insert each value into the BST

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)  # Traverse left subtree
        print(node.value, end = " ")  # Print the node value
        inorder_traversal(node.right)  # Traverse right subtree

print("Inorder Traversal (Sorted Output): ")
inorder_traversal(root)