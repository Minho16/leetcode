# 23. Merge k Sorted Lists
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # O(n*m) solutions n = len(lists), m = number of elements in lists
    # Solution uses a auxiliary list to store the head value of each linked list
    # then appends the minimum value to the list ('head') that will be returned
    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        s = ListNode("start")
        head = s
        head_vals = []
        for node in lists:
            if node:
                head_vals.append(node.val)
            else:
                head_vals.append(1000000)
        while sum(head_vals) < len(lists) * 1000000:
            min_val = min(head_vals)
            i = head_vals.index(min_val)
            head.next = ListNode(lists[i].val, None)
            head = head.next
            if lists[i].next:
                head_vals[i] = lists[i].next.val
                lists[i] = lists[i].next
            else:
                head_vals[i] = 1000000
        return s.next

    # Solution of complexity O(m*log(m)), m = number of elements in lists
    # The problem of this solution is that it does not use the fact of the list being already ordered
    # and sorts it again. It also converts the linked list to a regular list to then create the returning
    # linked list.
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        s = ListNode("start")
        head = s
        node_vals = []
        for linked in lists:
            while linked:
                node_vals.append(linked.val)
                linked = linked.next
        node_vals = sorted(node_vals)
        for node in node_vals:
            head.next = ListNode(node, None)
            head = head.next
        return s.next


s = Solution()
l1 = ListNode(1, ListNode(4, ListNode(5, None)))
l2 = ListNode(1, ListNode(3, ListNode(4, None)))
l3 = ListNode(2, ListNode(6, None))
r = s.mergeKLists([l1, l2, l3])

[1, 1, 2, 3, 4, 4, 5, 6]
