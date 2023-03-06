class Solution:
    def decodeString2(self, s: str) -> str:
        stack = []
        res = ''
        for i,char in enumerate(s):
            if char.isnumeric():
                if len(stack) > 0 and stack[-1].isnumeric():
                    stack[-1] += char                    
                else:
                    stack.append(char)
            elif len(stack) == 0:
                res += char
            elif char != '[' and char != ']':
                if stack[-1].isnumeric():
                    stack.append(char)
                else:
                    stack[-1] += char
            elif char == ']':
                string = stack.pop()
                n = int(stack.pop())
                if len(stack) > 0:
                    stack[-1] += string*n
                else:
                    res += string*n
        return res
    
    # Second try, a different way to solve the problem (let's hope with less if's)
    # Need to finish implementation
    def decodeString(self, s: str) -> str:
        res = ''
        stack = []
        i = 0
        num = ''
        word = ''
        while i < len(s):
            if s[i] == '[':
                stack.append(num)
                num = ''
            elif s[i].isnumeric():
                num += s[i]
            elif s[i] != ']':
                word += s[i]
            else:
                if len(stack) == 1:
                    res += int(stack.pop())*word
                else:
                    res += word




            i += 1


        return res

s = Solution()
# r = s.decodeString("3[a]2[bc]")
# print(r, r == "aaabcbc") 

# r = s.decodeString("3[a2[c]]")
# print(r, r == "accaccacc")

# r = s.decodeString("2[abc]3[cd]ef")
# print(r, r == "abcabccdcdcdef")


# r = s.decodeString("100[leetcode]")
# print(r)

r = s.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")
print(r, r=="zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef")