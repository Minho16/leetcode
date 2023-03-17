# 19. Remove Nth Node From End of List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        copy = head
        c = 0
        # Count the number of nodes while conserving the information of them
        while copy:
            copy = copy.next
            c += 1
        iter = c - n
        copy = head
        # Fill the linked list
        while copy:
            # Do not insert the node we want to remove
            if iter == 0:
                copy = copy.next
            copy = copy.next
        return head
