class Solution:
    # Runtime: 37 ms (87.74%) | Memory: 13.9 MB (68.18%)
    # O(2*n) = O(n) solution
    def getHint(self, secret: str, guess: str) -> str:
        d = {}
        bulls = 0
        vis = [0]*len(secret)
        # Store occurrences of each char that is not bull
        for i, c in enumerate(secret):
            if c != guess[i]:
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1
                vis[i] = 0
            else:
                # Increment bulls
                bulls += 1
                vis[i] = 1

        cows = 0
        for i, c in enumerate(guess):
            # If c can be a cow and the index is not a bull
            if  c in d and d[c] > 0 and vis[i] == 0:
                cows += 1
                d[c] -= 1
        return str(bulls)+'A'+str(cows)+'B'

s = Solution()
r = s.getHint('1123', '0111')
print(r, r=='1A1B')

r = s.getHint('8170', '8701')
print(r, r =='1A3B')

r = s.getHint('11', '10')
print(r, r == '1A0B')
