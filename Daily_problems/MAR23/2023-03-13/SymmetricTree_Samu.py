from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        l = [root]
        while len(l) > 0:
            l2 = []
            vals = []
            for node in l:
                if node.right:
                    l2.append(node.right)
                    vals.append(node.right.val)
                else:
                    vals.append(None)
                if node.left:
                    vals.append(node.left.val)
                    l2.append(node.left)
                else:
                    vals.append(None)
            if vals != vals[::-1]:
                return False
            l = l2
        return True