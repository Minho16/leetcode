class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_function(n):
            s = 0
            while n:
                s += (n % 10) ** 2
                n = n // 10
            return s

        slow = sum_function(n)
        fast = sum_function(sum_function(n))
        while slow != 1 and slow != fast:
            slow = sum_function(slow)
            fast = sum_function(sum_function(fast))
        if slow == 1 or fast == 1:
            return True
        return False


s = Solution()
r = s.isHappy(2)
print(r)
