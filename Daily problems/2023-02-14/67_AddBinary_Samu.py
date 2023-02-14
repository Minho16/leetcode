class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = 1
        carry = 0
        la= len(a)
        lb= len(b)
        s = ''
        if lb > la:
            la, lb = lb, la
            a, b = b, a

        while i <= la or i <= lb:
            if i <= la and i <= lb:
                r = ''
                if a[-i] == b[-i] and carry:
                    r = '1'
                    carry = int(a[-i])
                elif a[-i] == b[-i]:
                    r = '0'
                    carry = int(a[-i])
                elif carry:
                    r = '0'
                    carry = 1
                else:
                    r = '1'
            elif i <= la:
                r = ''
                if a[-i] == '0' and carry:
                    r = '1'
                    carry = 0
                elif a[-i] == '0':
                    r = '0'
                elif a[-i] == '1'  and carry:
                    r = '0'
                    carry = 1
                else:
                    r = '1'                
            s = r + s
            i += 1
        if carry:
            s = '1'+s
        return s


s = Solution()
r = s.addBinary("1100", "1")
print(r, r=="1101")
r = s.addBinary("1010", "1011")
print(r, r=="10101")