# 43. Multiply Strings
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        t = 0
        for num in num2:
            s = 0
            n = int(num)
            for c in num1:
                s = s*10+n*int(c)
            t = t*10 +s
        return str(t)
print(Solution().multiply('123', '456'))