from Reorder_Routes_to_Make_All_Paths_Lead_to_the_City_Zero_Minho import Solution


class TestSolution:
    def test_minReorder(self):
        sol = Solution()

        # Test Case 1
        n = 6
        connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
        assert sol.minReorder(n, connections) == 3

        # Test Case 2
        n = 5
        connections = [[1,0],[1,2],[3,2],[3,4]]
        assert sol.minReorder(n, connections) == 2

        # Test Case 3
        n = 3
        connections = [[1,0],[2,0]]
        assert sol.minReorder(n, connections) == 0
