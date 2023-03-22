# 2492. Minimum Score of a Path Between Two Cities
from typing import List
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # The graf will be stored in an adjancency list
        visited = [0 for i in range(n+1)]
        adj_list = {}
        min_road_val = {}
        # adj_list[i] : Stores all the nodes that can be reached from node i
        # min_road_val[i] : Stores the minimum value of the roads that can be reached from node i
        for a, b, distance in roads:
            if a not in adj_list:
                adj_list[a] = [b]
                min_road_val[a] = distance
            else:
                adj_list[a].append(b)
                min_road_val[a] = min(min_road_val[a], distance)

            if b not in adj_list:
                adj_list[b] = [a]
                min_road_val[b] = distance
            else:
                adj_list[b].append(a)
                min_road_val[b] = min(min_road_val[b], distance)

        reach = [min_road_val[1]]
        to_visit = [1]
        while len(to_visit) > 0:
            t2 = []
            for a in to_visit:
                visited[a] = 1
                for b in adj_list[a]:
                    if not visited[b]:
                        reach.append(min_road_val[b])
                        t2.append(b)
            to_visit = t2



        retur=min(reach)
        print(retur)
        return retur


class Solution2:
    def __init__(self) -> None:
        self.graf = []
        self.visited = []
        self.sz = 0
    # First approach, TLE
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # The will be stored in an sparse matrix
        self.graf = [[1000000 for i in range(n)] for j in range(n)]
        self.visited = [0 for i in range(n)]
        self.sz = n
        for a, b, distance in roads:
            self.graf[a-1][b-1] = distance
            self.graf[b-1][a-1] = distance

        def explore(node):
            min_v = 100000
            # Minim value of all adjacent nodes
            self.visited[node] = 1
            min_v = min(self.graf[node])
            # Apply recursion to all adjacent nodes
            for i in range(self.sz):
                if not self.visited[i] and self.graf[node][i] != 1000000:
                    self.graf[node][i] = 1000000
                    self.graf[i][node] = 1000000
                    min_v = min(min_v, explore(i))
            return min_v

        retur=explore(0)
        print(retur)
        return retur





Solution().minScore(9, [[6,2,7],[3,7,2],[9,6,5],[2,4,9],[7,8,7],[8,4,5],[1,6,10]])

Solution().minScore(4, [[1,2,3],[1,3,4],[2,4,2],[3,4,2]])

Solution().minScore(6, [[4,5,7468],[6,2,7173],[6,3,8365],[2,3,7674],[5,6,7852],[1,2,8547],[2,4,1885],[2,5,5192],[1,3,4065],[1,4,7357]])
