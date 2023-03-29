# 1466. Reorder Routes to Make All Paths Lead to the City Zero
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Adj_list[i] contains the nodes that can reach directly to node i
        out_edges = [[] for i in range(n)]
        in_edges = [[] for i in range(n)]
        for a, b in connections:
            out_edges[a].append(b)
            in_edges[b].append(a)

        check = [0]
        res = 0

        visited = [False]*n
        while len(check) > 0:
            c2 = []
            for node in check:
                visited[node] = True

                out = []
                for n in out_edges[node]:
                    if not visited[n]:
                        out.append(n)
                        res += 1
                inc = []

                for n in in_edges[node]:
                    if not visited[n]:
                        inc.append(n)

                c2 = c2 + out + inc
            check = c2
        return res
