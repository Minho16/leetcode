from MinimumScoreOfAPathBetweenTwoCities_Samu import Solution
def test_minScore():
    s = Solution()

    # Test case 1
    n = 5
    roads = [[1,2,5],[1,3,1],[3,4,1],[4,5,1],[2,5,5]]
    assert s.minScore(n, roads) == 1

    # Test case 2
    n = 4
    roads = [[1,2,3],[1,3,4],[2,4,2],[3,4,2]]
    assert s.minScore(n, roads) == 2

    # Test case 3
    n = 3
    roads = [[1,2,3],[2,3,1]]
    assert s.minScore(n, roads) == 1

    # Test case 4
    n = 2
    roads = [[1,2,1]]
    assert s.minScore(n, roads) == 1

    # Test case 5
    n = 6
    roads = [[1,2,1],[1,3,2],[2,4,2],[2,5,1],[3,4,1],[4,5,1],[5,6,1]]
    assert s.minScore(n, roads) == 1

    print("All test cases pass")
