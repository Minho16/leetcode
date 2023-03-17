from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Linear complexity, O(1) space. (Runtime: 27 ms (92.8%) |  )
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inOrder(root):
            if root is None:
                return
            root.right, root.left = root.left, root.right
            inOrder(root.left)
            inOrder(root.right)

        inOrder(root)
        return root


s = Solution()
r = TreeNode(
    4,
    TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)),
    TreeNode(7, TreeNode(6, None, None), TreeNode(9, None, None)),
)
s.invertTree(r)
