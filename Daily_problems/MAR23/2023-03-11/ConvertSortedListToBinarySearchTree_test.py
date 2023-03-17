from typing import Optional

from ConvertSortedListToBinarySearchTree_Samu import ListNode, Solution, TreeNode


class TestSolution:
    def test_detectCycle_with_cycle(self):
        # create an instance of the Solution class
        solution = Solution()

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

        tree5 = TreeNode(5, None, None)
        tree10 = TreeNode(-10, None, None)
        tree3 = TreeNode(-3, tree10, None)
        tree9 = TreeNode(9, tree5, None)
        tree0 = TreeNode(0, tree3, tree9)

        # call the detectCycle function
        result = solution.sortedListToBST(node1)

        # check that the result is tree0
        assert self.is_same_tree(result, tree0)

    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return (
            p.val == q.val
            and self.is_same_tree(p.left, q.left)
            and self.is_same_tree(p.right, q.right)
        )


def test_sortedListToBST():
    solution = Solution()

    # Test case 1: Input linked list with 3 elements
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    result = solution.sortedListToBST(head)
    assert result.val == 2
    assert result.left.val == 1
    assert result.right.val == 3
