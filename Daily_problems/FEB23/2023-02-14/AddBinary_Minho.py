class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_num = int(a, 2)
        b_num = int(b, 2)
        total_sum = a_num + b_num
        return bin(total_sum)[2:]


s = Solution()
r = s.addBinary("1100", "1")
print(r, r == "1101")
r = s.addBinary("1010", "1011")
print(r, r == "10101")
