import pytest

from Maximum_Depth_of_Binary_Tree import Solution, TreeNode


@pytest.fixture
def tree():
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root


def test_max_depth(tree):
    solution = Solution()
    assert solution.maxDepth(tree) == 3


def test_max_depth_empty():
    solution = Solution()
    assert solution.maxDepth(None) == 0
