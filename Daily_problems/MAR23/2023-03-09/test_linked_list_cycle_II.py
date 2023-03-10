from Linked_List_Cycle_II_Minho import Solution
# from LinkedListCycleII_Samu import Solution

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TestSolution:
    def test_detectCycle_with_cycle(self):
        # create a linked list with a cycle
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2

        # create an instance of the Solution class
        solution = Solution()

        # call the detectCycle function
        result = solution.detectCycle(node1)

        # check that the result is node2
        assert result == node2

    def test_detectCycle_without_cycle(self):
        # create a linked list without a cycle
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = None

        # create an instance of the Solution class
        solution = Solution()

        # call the detectCycle function
        result = solution.detectCycle(node1)

        # check that the result is None
        assert result == None