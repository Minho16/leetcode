from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        d = 1
        def dfs(root, d):
            if root is None or (root.left is None and root.right is None):
                return d
            else:
                return max(dfs(root.right, d+1), dfs(root.left, d+1))
        
        return dfs(root, d)

s = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
r = s.maxDepth(root)
print(r, r==3)

root = TreeNode(1, None, TreeNode(2))
r = s.maxDepth(root)
print(r, r==2)
