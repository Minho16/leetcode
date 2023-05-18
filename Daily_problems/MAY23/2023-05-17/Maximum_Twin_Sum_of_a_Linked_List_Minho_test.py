from Maximum_Twin_Sum_of_a_Linked_List_Minho import Solution, ListNode


def test_pairSum():
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    assert s.pairSum(head) == 7


def test_pairSum_two():
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(10)
    head.next.next = ListNode(100)
    head.next.next.next = ListNode(1000)
    head.next.next.next.next = ListNode(10000)
    head.next.next.next.next.next = ListNode(100000)

    assert s.pairSum(head) == 100001



# class Solution:
#     def pairSum(self, head):
#         slow = head
#         fast = head
#         maxVal = 0

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#         nextNode, prev = None, None
#         while slow:
#             nextNode = slow.next
#             slow.next = prev
#             prev = slow
#             slow = nextNode

#         while prev:
#             maxVal = max(maxVal, head.val + prev.val)
#             prev = prev.next
#             head = head.next

#         return maxVal
