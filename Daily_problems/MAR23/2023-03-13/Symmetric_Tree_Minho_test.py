from Symmetric_Tree_Minho import Solution, TreeNode


def test_isSymmetric():

    # Test case 1: Symmetric tree
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    assert solution.isSymmetric(root) == True

    # Test case 2: Asymmetric tree
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(3)
    assert solution.isSymmetric(root) == False

    # Test case 3: Empty tree
    solution = Solution()
    root = None
    assert solution.isSymmetric(root) == True