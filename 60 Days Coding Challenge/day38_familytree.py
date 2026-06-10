class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

inorder(root)