# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def __init__(self):
        self.total_sum = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        '''
            1. Sum to the total number if both left and right do not exist
            2. Implement DFS
        
        '''
        sum_of_nodes = ''
        self.DFS(root, sum_of_nodes)
    
        return self.total_sum


    def DFS(self, node, sum_of_nodes):
        if node == None:
            return
        
        sum_of_nodes += str(node.val)

        if node.left == None and node.right == None:
            self.total_sum += int(sum_of_nodes)
        
        self.DFS(node.left, sum_of_nodes)
        self.DFS(node.right, sum_of_nodes)

def test_sumNumbers():
    s = Solution()

    # Test for empty tree
    root = None
    result = s.sumNumbers(root)
    assert result == 0

    # Test for tree with one node
    root = TreeNode(val=1)
    result = s.sumNumbers(root)
    assert result == 1

    # Test for tree with multiple nodes
    root = TreeNode(val=4)
    node2 = TreeNode(val=9)
    node3 = TreeNode(val=0)
    node4 = TreeNode(val=5)
    node5 = TreeNode(val=1)
    root.left = node2
    root.right = node3
    node2.left = node4
    node2.right = node5

    result = s.sumNumbers(root)
    assert result == 1026