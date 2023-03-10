import random

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.random_values_list = []
        while head:
            self.random_values_list.append(head.val)
            head = head.next


    def getRandom(self) -> int:
        return random.choice(self.random_values_list)
