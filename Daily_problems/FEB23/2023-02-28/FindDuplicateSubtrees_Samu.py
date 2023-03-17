# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Suboptimal solution complexity O(n^2)
    def get_struct(self, node):
        struct = []
        line = [["val", node]]
        while len(line) > 0:
            new_line = []
            for pos, item in line:
                if item:
                    struct.append(pos + str(item.val))
                if item.left:
                    new_line.append(["left", item.left])
                else:
                    struct.append("leftNone")
                if item.right:
                    new_line.append(["right", item.right])
                else:
                    struct.append("rightNone")
            line = new_line
        return struct

    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        struct_list = []
        duplicates = []
        line = [root]
        struct_duplicate = []
        while len(line) > 0:
            new_line = []
            for node in line:
                s = self.get_struct(node)
                if s not in struct_list:
                    struct_list.append(s)
                elif s not in struct_duplicate:
                    struct_duplicate.append(s)
                    duplicates.append(node)
                struct_list.append(s)
                if node.left:
                    new_line.append(node.left)
                if node.right:
                    new_line.append(node.right)
            line = new_line
        return duplicates


s = Solution()
root = TreeNode(
    1,
    TreeNode(2, TreeNode(4, None, None), None),
    TreeNode(3, TreeNode(2, TreeNode(4, None, None), None), TreeNode(4, None, None)),
)
r = s.findDuplicateSubtrees(root)


# [0,0,0,0,null,null,0,null,null,null,0]
root = TreeNode(
    0,
    TreeNode(0, TreeNode(0, None, None), None),
    TreeNode(0, None, TreeNode(0, None, TreeNode(0, None, None))),
)
r = s.findDuplicateSubtrees(root)
