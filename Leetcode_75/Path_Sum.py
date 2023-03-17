# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def hasPathSum(self, root, targetSum) -> bool:
        if root == None:
            return False

        queue = deque([(root, targetSum)])

        while queue:
            node, totalSum = queue.popleft()

            if node is None:
                continue

            if not node.left and not node.right and totalSum == node.val:
                return True

            queue.append((node.left, totalSum - node.val))
            queue.append((node.right, totalSum - node.val))

        return False
