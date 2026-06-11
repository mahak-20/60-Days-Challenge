class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def buildTree(values, i=0):
    if i >= len(values) or values[i] == -1:
        return None

    root = TreeNode(values[i])

    root.left = buildTree(values, 2*i + 1)
    root.right = buildTree(values, 2*i + 2)

    return root
def maxDepth(root):
    if root is None:
        return 0

    leftDepth = maxDepth(root.left)
    rightDepth = maxDepth(root.right)

    return 1 + max(leftDepth, rightDepth)

values = list(map(int, input("Enter nodes (-1 for null): ").split()))
root = buildTree(values)
print("Maximum Depth =", maxDepth(root))