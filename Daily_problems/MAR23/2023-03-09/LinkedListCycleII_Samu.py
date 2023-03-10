class Solution(object):
    # 09-03-2023 Version
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head

        while slow and fast:
            if slow.next and fast.next and fast.next.next:
                slow = slow.next
            else:
                return None
            if slow == fast:
                check = head
                while check != slow:
                    check = check.next
                    slow = slow.next
                return check
        return None
    

    # 04-11-2022 Version
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head

        counter = -1
        if not slow or not slow.next:
            return None
        while fast.next and  slow.next and fast.next.next and counter == -1:
            if slow.next == fast.next.next:
                slow = slow.next
                fast = fast.next.next
                counter = 0
                while slow != fast.next:
                    counter += 1
                    fast = fast.next
            slow = slow.next
            fast = fast.next.next

        if counter != -1:
            slow = head
            while slow.next:
                fast = slow
                for i in range(counter+1):
                    fast = fast.next
                if fast == slow:
                    return slow
                slow = slow.next        
            return head.next
        return None
