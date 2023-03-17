from Sum_Root_to_Leaf_Numbers_Minho import Solution, TreeNode


def test_sumNumbers():
    # Test for empty tree
    s = Solution()
    root = None
    result = s.sumNumbers(root)
    assert result == 0

    # Test for tree with one node
    s = Solution()
    root = TreeNode(val=1)
    result = s.sumNumbers(root)
    assert result == 1

    # Test for tree with multiple nodes
    s = Solution()
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
