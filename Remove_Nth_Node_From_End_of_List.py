# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # add the values of linked list 
        node_values_list = []

        while head:
            node_values_list.append(head.val)
            head = head.next
        
        # remove the corresponding index
        node_values_list.pop(len(node_values_list) - n)


        # How to return an empty ListNode?
        if node_values_list == []:
            return None
        

        # Create a new linked_list with node_values_list
        head_new = ListNode(val=node_values_list[-1])
        parent_node = ListNode(val=node_values_list[-1])
        node_values_list.pop(-1)

        while node_values_list:
            parent_node = ListNode(val=node_values_list[-1], next=head_new)
            node_values_list.pop(-1)
            head_new = parent_node

        return parent_node


# Solution --> faster since it is not reading the linked list twice
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         fast = head
#         slow = head
#         # advance fast to nth position
#         for i in range(n):
#             fast = fast.next
            
#         if not fast:
#             return head.next
#         # then advance both fast and slow now they are nth postions apart
#         # when fast gets to None, slow will be just before the item to be deleted
#         while fast.next:
#             slow = slow.next
#             fast = fast.next
#         # delete the node
#         slow.next = slow.next.next
#         return head


def test_removeNthFromEnd():
    s = Solution()

    # Test for linked list with one node
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

