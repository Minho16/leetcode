class Solution:
    # O(n) complexity (Runtime: 23 ms (97.36%) | Memory: 13.9 MB (59.41%))
    def decodeString(self, s: str) -> str:
        res = ''
        stack = []
        num = ''
        word = ''
        for i, char in enumerate(s):
            if char == '[':
                stack.append(num)
                num = ''
            elif char.isnumeric():
                if word != '' and len(stack) > 0 and stack[-1].isnumeric():
                    stack.append(word)
                elif word != '' and len(stack) > 0:
                    stack[-1] += word
                word = ''
                num += char
            elif char != ']':
                if len(stack) == 0:
                    res += char
                    word = ''
                else:
                    word += char
            else:
                if len(stack) == 1:
                    res += int(stack.pop())*word
                    word = ''
                else:
                    if not stack[-1].isnumeric():
                        if word != '':
                            word = stack.pop() + word
                        else:
                            word = stack.pop()
                        
                    word = int(stack.pop())*word
                    if len(stack) > 0 and stack[-1].isnumeric():
                        stack.append(word)
                    elif len(stack) > 0:
                        stack[-1] += word
                    else:
                        res += word
                    word = ''
        return res

s = Solution()
r = s.decodeString("3[a]2[bc]")
print(r, r == "aaabcbc") 

# r = s.decodeString("3[a2[c]]")
# print(r, r == "accaccacc")

# r = s.decodeString("2[abc]3[cd]ef")
# print(r, r == "abcabccdcdcdef")


# r = s.decodeString("100[leetcode]")
# print(r)

# r = s.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")
# print(r)
# print("zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef")

r = s.decodeString("2[ab3[cd]]4[xy]")
print(r, r == "abcdcdcdabcdcdcdxyxyxyxy")