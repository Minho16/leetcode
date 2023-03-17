from typing import Optional

import pytest
from Construct_Binary_Tree_from_Inorder_and_Postorder_Traversal_Minho import (
    Solution,
    TreeNode,
)


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    return (
        p.val == q.val
        and is_same_tree(p.left, q.left)
        and is_same_tree(p.right, q.right)
    )


@pytest.mark.parametrize(
    "inorder,postorder,expected",
    [
        ([], [], None),
        ([1], [1], TreeNode(1)),
        (
            [9, 3, 15, 20, 7],
            [9, 15, 7, 20, 3],
            TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),
        ),
    ],
)
def test_buildTree(inorder, postorder, expected):
    solution = Solution()
    result = solution.buildTree(inorder, postorder)
    assert is_same_tree(result, expected)
