# 2316. Count Unreachable Pairs of Nodes in an Undirected Graph
from typing import List
class Solution:
    def __init__(self) -> None:
        self.adj_list = []
        self.visited = []
        self.islands = []

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        self.visited = [0]*n
        # Create adjancency list
        self.adj_list = [[] for _ in range(n)]
        for a, b in edges:
            self.adj_list[a].append(b)
            self.adj_list[b].append(a)

        # Visits all nodes that can be reached from 'node'
        def visit(node):
            self.visited[node] = True
            count = 1
            for neighbour in self.adj_list[node]:
                if not self.visited[neighbour]:
                    count += visit(neighbour)
            return count

        # Iter through all nodes
        alone = 0
        self.islands = []
        for node in range(n):
            if not self.visited[node]:
                if self.adj_list[node]:
                    self.islands.append(visit(node))
                else:
                    alone += 1
        # Number of isolated nodes (to avoid a list full of ones)
        if alone != 0:
            self.islands.append(alone)

        # Isolated computation
        res = 0
        for i in range(1, alone):
            res += i

        # Computation for the rest of islands
        for i in range(len(self.islands)-1):
            res += self.islands[i]*sum(self.islands[i+1:])
        return res

Solution().countPairs(5, [[0, 1], [1, 2], [3, 4]])
