from typing import Optional, List
from collections import deque
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Use a queue to store each level and the put them in a list of lists 
        if root is None:
            return None
        q = deque([root.val])
        l = [[root.val]]
        while len(q) > 0:
            q2 = deque()
            l2 = []
            while len(q) > 0:
                n = q.popleft()
                if n.left:
                    l2.append(n.left.val)
                    q2.append(n.left)
                if n.right:
                    l2.append(n.right.val)
                    q2.append(n.right)
            l.append(l2)
            q = q2
        return l
    
s = Solution()