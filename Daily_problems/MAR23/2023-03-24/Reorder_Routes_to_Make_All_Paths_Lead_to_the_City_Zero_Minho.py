# Time limit issue
class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        reorder_counter = 0
        visited_nodes = [0]

        while connections:
            a, b = connections[0]

            if a in visited_nodes and b not in visited_nodes:
                reorder_counter += 1
                visited_nodes.append(b)
            elif a not in visited_nodes and b in visited_nodes:
                visited_nodes.append(a)
            elif a not in visited_nodes and b not in visited_nodes:
                connections.append(connections[0])
            del connections[0]

        return reorder_counter
