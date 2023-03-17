# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root) -> int:
        """
        strategy: start with count level = 1
        stop when node == None -->
        """
        queue = deque([(root, 1)])  # node and level information

        while queue:
            node, curr_depth = queue.popleft()

            if node is None:
                continue

            if node.left is None and node.right is None:
                return curr_depth

            queue.append((node.left, curr_depth + 1))
            queue.append((node.right, curr_depth + 1))

        return 0
