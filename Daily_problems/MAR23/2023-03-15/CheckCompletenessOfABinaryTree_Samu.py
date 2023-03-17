from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Apprach that checks some conditions that will solve the problem
    # Most of the conditions are not optimal since there are more powerfull conditions that solve the problem with few lines of code
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        l1 = [root]
        while len(l1) > 0:
            l2 = []
            next = False
            n = 1
            complete = True
            for node in l1:
                left = False
                right = False
                if node.left:
                    left = True
                    l2.append(node.left)
                    if node.left.right or node.left.left:
                        next = True
                    if not complete:
                        return False
                if node.right:
                    right = True
                    l2.append(node.right)
                    if node.right.left or node.right.right:
                        next = True
                if right and not left:
                    return False
                if (left and not right) or (not left and not right):
                    complete = False
            if next and len(l2) < len(l1) * 2:
                return False
            l1 = l2
        return True


l = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), None))
Solution().isCompleteTree(l)
