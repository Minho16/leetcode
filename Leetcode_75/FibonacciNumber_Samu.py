import time
class Solution(object):
    # Recursive version, Makes too much recursion, not optimal
    def fib_rec(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        elif n < 2:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)

    # Linear version
    def fib(self, n):
        if n < 0:
            return 0
        elif n < 2:
            return 1
        i = 1
        f1 = 1
        f2 = 1
        while i < n:
            f1, f2 = f2, f1+f2
            i += 1
        return f2

# Fib_rec takes 26 seconds to print fib(35)
# Fib_linear takes 0.002 seconds to print(10000)
s = Solution()
start = time.time()
r = s.fib(10009)
end = time.time()
print(end-start, ' seconds')

s = Solution()
start = time.time()
r = s.fib(6)
end = time.time()
print(r, end-start, ' seconds')