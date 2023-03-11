from ConvertSortedListToBinarySearchTree_Samu import Solution, ListNode, TreeNode

class TestSolution:
    def test_detectCycle_with_cycle(self):
        # create a linked list with a cycle
        node1 = ListNode(-10)
        node2 = ListNode(-3)
        node3 = ListNode(0)
        node4 = ListNode(5)
        node5 = ListNode(9)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        tree10 = TreeNode(-10, None, None)
        tree3 = TreeNode(-3, tree10, None)
        tree5 = TreeNode(5, None, None)
        tree9 = TreeNode(9, tree5, None)
        tree0 = TreeNode(0, tree3, tree9)

        # create an instance of the Solution class
        solution = Solution()

        # call the detectCycle function
        result = solution.sortedListToBST(node1)

        # check that the result is tree0
        assert result == tree0