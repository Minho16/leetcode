import heapq
from typing import List


class Solution:
    # O(n*log(n)) Solution (Runtime: 54 ms (86.3%) | Memory: 13.9 MB (91.37%))
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1

        d = sorted(d.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        s = []
        i = d[0][1]
        q = []
        heapq.heapify(q)
        for key, val in d:
            if val == i:
                heapq.heappush(q, key)
            else:
                while q:
                    s.append(heapq.heappop(q))
                heapq.heappush(q, key)
                i = val
                if len(s) >= k:
                    return s[0:k]
        while q:
            s.append(heapq.heappop(q))
            if len(s) >= k:
                return s[0:k]
        return s[0:k]


s = Solution()
r = s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k=2)
print(r, r == ["i", "love"])

r = s.topKFrequent(
    words=["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k=4
)
print(r, r == ["the", "is", "sunny", "day"])
