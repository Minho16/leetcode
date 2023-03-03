class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i, char in enumerate(haystack):
            if char == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i        
        return -1
    

s = Solution()
r = s.strStr('sadbutsad', 'sad')
print(r, r==0)

r = s.strStr('leetcode', 'leeto')
print(r, r==-1)