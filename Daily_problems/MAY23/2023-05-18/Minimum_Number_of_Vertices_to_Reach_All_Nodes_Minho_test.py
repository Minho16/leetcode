from Minimum_Number_of_Vertices_to_Reach_All_Nodes_Minho import Solution


s = Solution()


def test_minimum_number_of_vertices():
    n = 6
    edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
    assert s.findSmallestSetOfVertices(n=n, edges=edges) == [0, 3]



def test_minimum_number_of_vertices_second():
    n = 5
    edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
    assert s.findSmallestSetOfVertices(n=n, edges=edges) == [0, 2, 3]
