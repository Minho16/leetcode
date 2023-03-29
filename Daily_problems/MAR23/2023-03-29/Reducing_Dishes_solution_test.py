from Reducing_Dishes_solution import Solution


def test_maxSatisfaction():
    sol = Solution()
    assert sol.maxSatisfaction([4, 3, 2]) == 20
    assert sol.maxSatisfaction([-1, -8, 0, 5, -9]) == 14
    assert sol.maxSatisfaction([1, 2, 3, 4, 5]) == 55
