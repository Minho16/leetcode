from Remove_Nth_Node_From_End_of_List import Solution, ListNode


def test_removeNthFromEnd():
    # Test for linked list with one node
    s = Solution()

    head = ListNode(val=1)
    result = s.removeNthFromEnd(head, 1)
    assert result is None

    # Test for linked list with multiple nodes
    head = ListNode(val=1)
    node2 = ListNode(val=2)
    node3 = ListNode(val=3)
    node4 = ListNode(val=4)
    node5 = ListNode(val=5)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    result = s.removeNthFromEnd(head, 2)
    values = []
    while result:
        values.append(result.val)
        result = result.next
    assert values == [1, 2, 3, 5]

    # Test for removing the first node
    result = s.removeNthFromEnd(head, 5)
    values = []
    while result:
        values.append(result.val)
        result = result.next
    assert values == [2, 3, 4, 5]
