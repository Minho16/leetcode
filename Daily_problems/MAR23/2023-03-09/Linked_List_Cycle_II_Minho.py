# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_to_return = None
        key_id_node_value_node_dict = {}

        while head:

            if id(head) in key_id_node_value_node_dict.keys():
                node_to_return = key_id_node_value_node_dict[id(head)]
                break
            else:
                key_id_node_value_node_dict[id(head)] = head
            
            head = head.next

        if node_to_return == None:
            return None
        return node_to_return
