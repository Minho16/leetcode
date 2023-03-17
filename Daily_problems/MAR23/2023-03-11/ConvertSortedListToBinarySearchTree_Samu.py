# 109. Convert Sorted List to Binary Search Tree
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.nodelist: list[ListNode] = []

    # Recursive method to create the binary tree using recursion.
    # This version saves the list as a global variable and
    # only passes the index at recursion
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        while head:
            self.nodelist.append(head.val)
            head = head.next

        def recursive(left, right):
            if right - left <= 0:
                return
            if right - left == 1:
                return TreeNode(self.nodelist[left], None, None)
            value = self.nodelist[left + (right - left) // 2]
            return TreeNode(
                value,
                recursive(left, left + (right - left) // 2),
                recursive(left + (right - left) // 2 + 1, right),
            )

        result = recursive(0, len(self.nodelist))
        return result

    # This second version passes the actual list so it
    # should be less efficient in terms of
    # memory allocation. Leetcode tests, though,
    # shows that the complexity is the same.
    def sortedListToBST2(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        left = []
        while head:
            left.append(head.val)
            head = head.next

        def recursive(left):
            sz = len(left)
            if sz == 0:
                return
            if sz == 1:
                return TreeNode(left[0], None, None)
            value = left[sz // 2]
            return TreeNode(value,
                            recursive(left[: sz // 2]),
                            recursive(left[sz // 2 + 1:]))

        return recursive(left)


node1 = ListNode(-10)
node2 = ListNode(-3)
node3 = ListNode(0)
node4 = ListNode(5)
node5 = ListNode(9)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

s = Solution()
right = s.sortedListToBST(node1)
