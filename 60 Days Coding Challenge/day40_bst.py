class TreeNode:
    def __init__(self, value):
        self.val = self.val
        self.left = None
        self.right = None

def isValidBST(root, low=float('-inf'), high=float('inf')):
    if root is None:
        return True
    if root.val <=low or root.value>=high:
        return False
    return (isValidBST(root.left, low, root.val)) and isValidBST(root.right, root.val, high)