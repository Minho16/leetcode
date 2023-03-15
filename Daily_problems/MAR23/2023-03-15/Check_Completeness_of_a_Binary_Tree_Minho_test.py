import pytest
from Check_Completeness_of_a_Binary_Tree_Minho import Solution, TreeNode

# Helper function to create a binary tree from a list of values
def list_to_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

# Test cases
@pytest.mark.parametrize("tree_values, expected", [
    ([1, 2, 3, 4, 5, 6], True),
    ([1, 2, 3, 4, 5, None, 7], False),
    ([1], True),
])

def test_isCompleteTree(tree_values, expected):
    solution = Solution()
    tree = list_to_tree(tree_values)
    result = solution.isCompleteTree(tree)
    assert result == expected
