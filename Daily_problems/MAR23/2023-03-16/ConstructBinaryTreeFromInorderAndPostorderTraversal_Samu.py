# 106. Construct Binary Tree from Inorder and Postorder Traversal
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def recursive(inorder, postorder):
            if not inorder:
                return None
            if len(inorder) == 1:
                return TreeNode(inorder[0])
            root = postorder[-1]
            i = 0
            while inorder[i] != root:
                i+= 1
            left= inorder[:i]
            left2 = inorder[i+1:] 
            
            right = postorder[:i]
            right2 = postorder[i:-1]
            return TreeNode(root, recursive(left, right), recursive(left2, right2)) 

        return recursive(inorder, postorder)

Solution().buildTree([9,3,15,20,7], [9,15,7,20,3])
# Solution().buildTree([1, 2], [2, 1])


# inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]

#
#   3
# 9     20
#     15   7

# [3,2,1] [3,2,1]
#   1
#  2
# 3

# [15,20,7] [15,7,20, 
#   20
# 15  7