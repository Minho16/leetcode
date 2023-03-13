class Solution(object):
    # This solutions uses the idea of converting the characters to its ASCII integer (ord function)
    # substract the ASCII integer of zero to obtain the actual value, and use a list of integers
    # from 0 to 9 that represent each position of the result.
    def multiply(self, num1, num2):
        res = [0] * (len(num1)+len(num2))
        for i in range(len(num1)-1, -1, -1):
            carry = 0
            for j in range(len(num2)-1, -1, -1):
                tmp = (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0')) + carry
                carry = (res[i+j+1]+tmp) // 10
                res[i+j+1] = (res[i+j+1]+tmp) % 10
            res[i] += carry
        res = ''.join(map(str, res))
        return '0' if not res.lstrip('0') else res.lstrip('0')