import pytest

from Minimum_Depth_of_Binary_Tree import Solution, TreeNode


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


def test_min_depth(tree):
    solution = Solution()
    assert solution.minDepth(tree) == 2


def test_min_depth_empty():
    solution = Solution()
    assert solution.minDepth(None) == 0


def test_min_depth_only_left_branch():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    solution = Solution()
    assert solution.minDepth(root) == 3


def test_min_depth_only_right_branch():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    solution = Solution()
    assert solution.minDepth(root) == 3
