# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head) -> int:
        numbers_list = []
        max_value = 0

        # read all the nodes of the linked list and save them inside a list
        while head:
            numbers_list.append(head.val)
            head = head.next

        # while numbers exist in the list, make the comparison
        while len(numbers_list) != 0:
            if numbers_list[0] + numbers_list[-1] > max_value:
                max_value = numbers_list[0] + numbers_list[-1]
            numbers_list.pop(0)
            numbers_list.pop(-1)

        return max_value
