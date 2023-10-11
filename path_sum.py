from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        found = False

        def dfs(node, accruedSum):
            if node is None:
                return False

            accruedSum = accruedSum + node.val

            if accruedSum == targetSum:
                found = True
                return found

            if not node.left and not node.right:
                return

            dfs(node.left, accruedSum)
            dfs(node.right, accruedSum)

        return found

        dfs(root, 0)
