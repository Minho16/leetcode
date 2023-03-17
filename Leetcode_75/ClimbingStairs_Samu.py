class Solution(object):
    # Recursive algorithm | Takes too long
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        def recursive(self, n):
            if n < 1:
                return 0
            if n <= 2:
                return n
            return recursive(n - 1) + recursive(n - 2)

        return recursive(n)

    # Using Fibonacci Sequence
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ones = 1
        twos = 1
        for i in range(n - 1):
            ones, twos = twos, ones + twos
        return twos
