# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        if not root:
            return self.depth
        self.DFS(root, count)
        return self.depth

    def DFS(self, node, count):
        if not node:
            if count > self.depth:
                self.depth = count
            return
        count += 1
        self.DFS(node.left, count)
        self.DFS(node.right, count)
