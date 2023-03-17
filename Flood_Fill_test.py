from Flood_Fill import Solution


def test_floodFill():
    # Test case 1
    sol = Solution()
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    assert sol.floodFill(
        image, sr, sc, color) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

    # Test case 2
    sol = Solution()
    image = [[0, 0, 0], [0, 1, 1]]
    sr = 1
    sc = 1
    color = 1
    assert sol.floodFill(image, sr, sc, color) == [[0, 0, 0], [0, 1, 1]]
