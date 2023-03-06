import time
class Solution:
    # Time limit exceeded Solution, Complexity O(n*k)
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n < 2:
            return n
        prev = s[0]
        max_l = 0
        for i in range(n):
            # print(i)
            if prev != s[i] or i == 0:
                j = i
                rem_k = k
                c = 0     
                while j < n and rem_k >= 0:
                    if j >= 0:
                        if s[j] != s[i]:
                            rem_k -= 1
                        if rem_k >= 0:
                            c += 1
                    j += 1
                j = i-1
                while j >= 0 and rem_k >= 0:
                    if s[j] != s[i]:
                            rem_k -= 1
                    if rem_k >= 0:
                        c += 1
                    j -= 1

                if c > max_l:
                    max_l = c
                prev = s[i]
        return max_l

    # Complexity O(n) Solution 
    # Runtime: 111 ms (89.23%) | Memory: 14 MB (13.5%))
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        # Store the occurrences of chars in the substring of max_len
        d = {s[i] : 1}
        val = 0
        while i < len(s)-1:
            i += 1
            # Append new char to d
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
            
            # Move 'j' to the right
            if d[s[j]] + k  <= i-j:
                d[s[j]] -= 1
                j += 1

            # If the observing char 'j' has bigger capacity update val
            val = max(d[s[j]] + k, val)
        return min(max(d[s[-1]] + k, val), len(s))
                




ss = Solution()
s = "BBBB"
k = 0
r = ss.characterReplacement(s, k)
print(r, r==4)

s = "ABCDEFAF"
k = 1
r = ss.characterReplacement(s, k)
print(r, r==3)
