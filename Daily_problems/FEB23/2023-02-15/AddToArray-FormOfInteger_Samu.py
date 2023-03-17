class Solution(object):
    # "Faster" approach (Runtime 18.8% | Memory 7.26%)
    def addToArrayForm(self, num, k):
        a = ""
        for n in num:
            a += str(n)
        a = int(a) + k
        s = []
        while a:
            s.append(a % 10)
            a = a // 10
        return list(reversed(s))

    # Algorithmic approach / Lots of lists sums (Runtime 19.8% | Memory 35.31%)
    def addToArrayForm_alg(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """

        r = []
        i = 1
        carry = 0
        # Make the sum of k and num
        while k and i <= len(num):
            r = [(k % 10 + num[-i] + carry) % 10] + r
            if k % 10 + num[-i] + carry >= 10:
                carry = 1
            else:
                carry = 0
            k = k // 10
            i += 1

        # If k has a bigger order than num
        while k:
            r = [(k % 10 + carry) % 10] + r
            if k % 10 + carry >= 10:
                carry = 1
            else:
                carry = 0
            k = k // 10

        # If num has a bigger order than k
        while i <= len(num):
            r = [(num[-i] + carry) % 10] + r
            if num[-i] + carry >= 10:
                carry = 1
            else:
                carry = 0
            i += 1

        # Insert last carry
        if carry:
            r = [1] + r
        return r


s = Solution()
r = s.addToArrayForm([1, 2, 0, 0], 34)
print(r, r == [1, 2, 3, 4])

r = s.addToArrayForm([1, 2, 0, 0], 1234)
print(r, r == [2, 4, 3, 4])


r = s.addToArrayForm([1, 2, 0, 0], 8834)
print(r, r == [1, 0, 0, 3, 4])

r = s.addToArrayForm([0], 8834)
print(r, r == [8, 8, 3, 4])

r = s.addToArrayForm([9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 1)
print(r, r == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

r = s.addToArrayForm([7], 993)
print(r, r == [1, 0, 0, 0])
