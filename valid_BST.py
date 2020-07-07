# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return True

        return self.isValidBST(root.left) and self.isValidBST(root.right)
