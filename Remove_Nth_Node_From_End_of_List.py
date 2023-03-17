# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int):
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
