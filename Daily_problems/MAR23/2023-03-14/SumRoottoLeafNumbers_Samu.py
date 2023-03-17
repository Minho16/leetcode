# 129. Sum Root to Leaf Numbers
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Runtime 24 ms (97.50%) | Memory 13.8 MB (95.89%)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def recursive(tree, prev):
            if tree:
                # Adds the number at each node
                prev = prev * 10 + tree.val
                # If it is a leaf, return the num
                if tree.right is None and tree.left is None:
                    return prev
                # If it is none, keep searching
                return recursive(tree.right, prev) + recursive(tree.left, prev)
            # No node to return
            return 0

        return recursive(root, 0)


print(Solution().sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3))))
