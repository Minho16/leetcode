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
        self.nodelist = []

    # Recursive method to create the binary tree using recursion.
    # This version saves the list as a global variable and only passes the index at recursion
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        while head:
            self.nodelist.append(head.val)
            head = head.next

        def recursive(l, r):
            if r - l <= 0:
                return
            if r - l == 1:
                return TreeNode(self.nodelist[l], None, None)
            value = self.nodelist[l + (r - l) // 2]
            return TreeNode(
                value,
                recursive(l, l + (r - l) // 2),
                recursive(l + (r - l) // 2 + 1, r),
            )

        result = recursive(0, len(self.nodelist))
        return result

    # This second version passes the actual list so it should be less efficient in terms of
    # memory allocation. Leetcode tests, though, shows that the complexity is the same.
    def sortedListToBST2(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next

        def recursive(l):
            sz = len(l)
            if sz == 0:
                return
            if sz == 1:
                return TreeNode(l[0], None, None)
            value = l[sz // 2]
            return TreeNode(value, recursive(l[: sz // 2]), recursive(l[sz // 2 + 1 :]))

        return recursive(l)


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
r = s.sortedListToBST(node1)
