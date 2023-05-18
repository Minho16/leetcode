class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        edge_indexes = set([i for i in range(n)])

        for edge in edges:
            if edge[1] in edge_indexes:
                edge_indexes.remove(edge[1])

        return list(edge_indexes)


# Solution, not that much different
# class Solution:
#     def findSmallestSetOfVertices(self, n, edges):
#         indegree = [0] * n
#         for edge in edges:
#             indegree[edge[1]] += 1

#         ans = []
#         for i in range(n):
#             if indegree[i] == 0:
#                 ans.append(i)

#         return ans
