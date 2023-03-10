class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for char in s:
            if char == '#' and len(stack) > 0:
                stack.pop()
            elif char != '#':
                stack.append(char)
        stack1 = []
        for char in t:
            if char == '#' and len(stack1) > 0:
                stack1.pop()
            elif char != '#':
                stack1.append(char)
        return stack == stack1
    
s = Solution()
r = s.backspaceCompare("ab#c", "ad#c")
print(r) #True

r = s.backspaceCompare("ab##", "c#d#")
print(r) #True

r = s.backspaceCompare("a#c", "b")
print(r) #False